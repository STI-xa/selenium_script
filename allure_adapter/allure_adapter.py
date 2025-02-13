import functools
import inspect
import os
from datetime import datetime

import allure
import allure_commons
from allure_commons.logger import AllureFileLogger
from allure_commons.model2 import (TestResult,
                                   TestStepResult,
                                   Status,
                                   StatusDetails)
from allure_commons.reporter import AllureReporter
from allure_commons.utils import uuid4, now

reporter = AllureReporter()
log_dir = 'allure_results'
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

screenshot_dir = os.path.join(log_dir, 'screenshots')
if not os.path.exists(screenshot_dir):
    os.makedirs(screenshot_dir)

file_logger = AllureFileLogger(log_dir)
allure_commons.plugin_manager.register(file_logger)


def allure_step(step_name_w_value):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            case_uuid = uuid4()
            test_case = TestResult(uuid=case_uuid, start=now())

            calling_func = get_calling_func()
            test_case.description = calling_func

            reporter.schedule_test(case_uuid, test_case)
            current_step_uuid = uuid4()

            try:
                result = func(self, *args, **kwargs)
                step_name = get_func_args(func,
                                          self,
                                          step_name_w_value,
                                          *args,
                                          **kwargs)
                test_case.name = step_name
                step_result = TestStepResult(
                    name=step_name,
                    start=now())
                current_step_uuid = uuid4()
                reporter.start_step(None,
                                    current_step_uuid,
                                    step_result)

                get_screenshot(self, step_name, case_uuid)
                reporter.stop_step(current_step_uuid,
                                   stop=now(),
                                   status=Status.PASSED)
                test_case.status = Status.PASSED

            except Exception as e:
                step_name = get_func_args(func,
                                          self,
                                          step_name_w_value,
                                          *args,
                                          **kwargs)
                test_case.name = step_name
                step_result = TestStepResult(name=step_name, start=now())
                reporter.start_step(case_uuid, current_step_uuid, step_result)
                get_screenshot(self, step_name, case_uuid)
                reporter.stop_step(current_step_uuid,
                                   stop=now(),
                                   status=Status.FAILED,
                                   statusDetails=StatusDetails(message=str(e)))
                test_case.status = Status.FAILED
                test_case.statusDetails = StatusDetails(message=str(e))
                raise e

            finally:
                test_case.stop = now()
                reporter.close_test(case_uuid)

            return result

        return wrapper

    return decorator


def get_screenshot(self, step_name, case_uuid):
    driver = self.driver
    if driver is None:
        raise ValueError

    step_name = step_name.replace(' ', '_')
    date_time = datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
    screenshot_path = os.path.join(screenshot_dir,
                                   f'{step_name}_{date_time}.png')
    driver.save_screenshot(screenshot_path)
    reporter.attach_file(uuid=case_uuid,
                         source=screenshot_path,
                         name=step_name,
                         attachment_type=allure.attachment_type.PNG)


def get_calling_func():
    stack = inspect.stack()
    calling_func = None
    for frame_info in stack:
        if frame_info.function.startswith('test_'):
            calling_func = frame_info.function
            break
    return calling_func


def get_func_args(func, self, step_name_w_value, *args, **kwargs):
    func_args = inspect.signature(func).bind(self, *args, **kwargs)
    func_args.apply_defaults()
    get_function_args = step_name_w_value.format(**func_args.arguments)
    return get_function_args
