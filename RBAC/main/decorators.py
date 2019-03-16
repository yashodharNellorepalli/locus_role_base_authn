from .utils.helpers import get_request, get_error_response
from main.models import User, Role, Resource, ActionType
from .utils.messages import USER_DOES_NOT_EXIST, ROLE_DOES_NOT_EXIST, RESOURCE_DOES_NOT_EXIST, \
    ACTION_TYPE_DOES_NOT_EXIST
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST


def decorator_user(callback):
    def wrapper(*args, **kwargs):
        request = get_request(args)

        request_type_get = request.method == 'GET'
        user_id = request_type_get and request.query_params.get('user_id') or request.data.get('user_id')

        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response(get_error_response(USER_DOES_NOT_EXIST), status=HTTP_400_BAD_REQUEST)

        request.user = user

        return callback(*args, **kwargs)

    return wrapper


def decorator_role(callback):
    def wrapper(*args, **kwargs):
        request = get_request(args)

        request_type_get = request.method == 'GET'
        role_id = request_type_get and request.query_params.get('role_id') or request.data.get('role_id')

        try:
            role = Role.objects.get(id=role_id)
        except Role.DoesNotExist:
            return Response(get_error_response(ROLE_DOES_NOT_EXIST), status=HTTP_400_BAD_REQUEST)

        request.role = role

        return callback(*args, **kwargs)

    return wrapper


def decorator_resource(callback):
    def wrapper(*args, **kwargs):
        request = get_request(args)

        request_type_get = request.method == 'GET'
        resource_id = request_type_get and request.query_params.get('resource_id') or request.data.get('resource_id')

        try:
            resource = Resource.objects.get(id=resource_id)
        except Resource.DoesNotExist:
            return Response(get_error_response(RESOURCE_DOES_NOT_EXIST), status=HTTP_400_BAD_REQUEST)

        request.resource = resource

        return callback(*args, **kwargs)

    return wrapper


def decorator_action_type(callback):
    def wrapper(*args, **kwargs):
        request = get_request(args)

        request_type_get = request.method == 'GET'
        action_type_id = request_type_get and request.query_params.get('action_type_id') or request.data.get(
            'action_type_id')

        try:
            action_type = ActionType.objects.get(id=action_type_id)
        except ActionType .DoesNotExist:
            return Response(get_error_response(ACTION_TYPE_DOES_NOT_EXIST), status=HTTP_400_BAD_REQUEST)

        request.action_type = action_type

        return callback(*args, **kwargs)

    return wrapper
