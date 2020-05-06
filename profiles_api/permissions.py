from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """ """
    def has_object_permission(self, request, view, obj):
        """ Check auth user has the right to do the requested action """

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id

class UpdateOwnStatus(permissions.BasePermission):
    """Limit ProfileFeedItem's updates to user's owned"""

    def has_object_permission(self, request, view, obj):
        """Check update is made by logged user or is safe"""

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id == request.user.id
