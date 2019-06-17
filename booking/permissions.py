from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """ Класс IsOwnerOrReadOnly позволяет ограничить редактирование и удаление
    бронирования для всех пользователей, кроме автора
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user
