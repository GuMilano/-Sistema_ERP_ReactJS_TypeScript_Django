from rest_framework.exceptions import APIException

class NotFoundEmployee(APIException):
    status_code = 404
    default_detail = 'Employee not found.'
    default_code = 'not_found_employee'

class NotFoundGroup(APIException):
    status_code = 404
    default_detail = 'Group not found.'
    default_code = 'not_found_group'

class RequiredFields(APIException):
    status_code = 400
    default_detail = 'Required fields are missing.'
    default_code = 'required_fields'

class NotFoundTaskStatus(APIException):
    status_code = 404
    default_detail = 'Task status not found.'
    default_code = 'not_found_task_status'

class NotFoundTask(APIException):
    status_code = 404
    default_detail = 'Task not found.'
    default_code = 'not_found_task'