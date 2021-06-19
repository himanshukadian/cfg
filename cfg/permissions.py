from django.contrib.auth.models import Group
from django.db.models import Q
from rest_framework import permissions


def is_in_group(user, group_name):
    """
    Takes a user and a group name, and returns `True` if the user is in that group.
    """
    try:
        return Group.objects.get(name=group_name).user_set.filter(id=user.id).exists()
    except Group.DoesNotExist:
        return None


class HasGroupPermission(permissions.BasePermission):
    """
    Ensure user is in required groups.
    """

    def has_permission(self, request, view):
        # Get a mapping of methods -> required group.
        required_groups_mapping = getattr(view, "required_groups", {})

        # Determine the required groups for this particular request method.
        required_groups = required_groups_mapping.get(request.method, [])

        # Return True if the user has all the required groups or is staff.
        return all([is_in_group(request.user, group_name) if group_name != "__all__" else True for group_name in
                    required_groups]) or (request.user and request.user.is_staff)


class UserIsMentorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.groups.filter(name='2').exists()


class UserIsTeamOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.groups.filter(name='0').exists()


class UserIsTeamMemberOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.groups.filter(name='1').exists()


class UserIsTeamMember(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='1').exists()

class IsTeam(permissions.BasePermission):
    def has_permission(self, request, view):
        print("hellopem")
        return request.user.groups.filter(name=0).exists()


class IsTeamMember(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name=1).exists()


class Ismentor(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name=2).exists()


class IsRootModOrAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(Q(name=0) | Q(name=1)).exists()

# example view
# class MyView(APIView):
#     permission_classes = [HasGroupPermission]
#     required_groups = {
#         'GET': ['moderators', 'members'],
#         'POST': ['moderators', 'someMadeUpGroup'],
#         'PUT': ['__all__'],
#     }
