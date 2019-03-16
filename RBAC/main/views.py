from rest_framework.decorators import api_view
from .models import UserRole, ResourceActionTypeRole
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.response import Response
from .utils.helpers import get_error_response
from .utils.messages import USER_ROLE_ALREADY_EXIST, USER_ROLE_DOES_NOT_EXIST
from decorators import decorator_user, decorator_role, decorator_resource, decorator_action_type


@api_view(['POST'])
@decorator_user
@decorator_role
def assign_role_to_user(request):
    user = request.user
    role = request.role

    if UserRole.objects.filter(user=user, role=role).exists():
        return Response(get_error_response(message=USER_ROLE_ALREADY_EXIST), status=HTTP_400_BAD_REQUEST)

    UserRole.objects.create(user=user, role=role)

    response_data = {
        'status': True,
        'message': 'Successfully assigned role to user'
    }

    return Response(response_data)


@api_view(['POST'])
@decorator_user
@decorator_role
def remove_role_of_user(request):
    user = request.user
    role = request.role

    if not UserRole.objects.filter(user=user, role=role).exists():
        return Response(get_error_response(message=USER_ROLE_DOES_NOT_EXIST), status=HTTP_400_BAD_REQUEST)

    UserRole.objects.filter(user=user, role=role).delete()

    response_data = {
        'status': True,
        'message': 'Successfully role removed of User'
    }

    return Response(response_data)


@api_view(['GET'])
@decorator_user
@decorator_resource
@decorator_action_type
def check_user_action_type_from_resource(request):
    user = request.user
    resource = request.resource
    action_type = request.action_type

    user_role_ids = ResourceActionTypeRole.objects.filter(resource=resource, action_type=action_type).\
        values_list('role__role_of_user_roles__user__id', flat=True)

    user_action_type_from_resource = user.id in user_role_ids

    response_data = {
        'status': True,
        'user_action_type_from_resource': user_action_type_from_resource
    }

    return Response(response_data)