from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from .views import assign_role_to_user, remove_role_of_user, check_user_action_type_from_resource

router = DefaultRouter()

urlpatterns = router.urls

urlpatterns += [
    url(r'^assign_role_to_user/$', assign_role_to_user),
    url(r'^remove_role_of_user/$', remove_role_of_user),
    url(r'^check_user_action_type_from_resource/$', check_user_action_type_from_resource),
]
