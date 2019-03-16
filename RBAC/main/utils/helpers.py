from rest_framework.request import Request


def get_error_response(message, status=False):
    return {
        'status': status,
        'message': message
    }


def get_request(args):
    for argument in args:
        if isinstance(argument, Request):
            return argument

    return None
