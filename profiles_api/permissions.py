from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """ """
    def has_object_permission(self, request, view, obj):
        """ Check auth user has the right to do the requested action """

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id
