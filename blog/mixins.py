from django.core.exceptions import PermissionDenied


class PermsRequiredMixin:
    """
    :param perms: list of permission strings
    """
    perms = None

    def dispatch(self, request, *args, **kwargs):
        if request.user.has_perms(perm_list=self.perms):
            return super().dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied


class GroupsRequiredMixin:
    """
    :param groups: list of group strings
    """
    groups = None

    def dispatch(self, request, *args, **kwargs):
        if request.user.in_groups(self.groups, self.request.user):
            return super().dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied