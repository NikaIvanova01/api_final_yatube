from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrReadOnly(BasePermission):
    """
    Разрешает безопасные методы (GET, HEAD, OPTIONS) для всех пользователей.
    Запись (PUT, PATCH, DELETE) разрешена только автору объекта.
    """

    def has_permission(self, request, view):
        # Разрешаем аутентифицированным пользователям список и создание
        return request.user.is_authenticated or request.method in SAFE_METHODS

    def has_object_permission(self, request, view, obj):
        # Всегда разрешаем безопасные методы
        if request.method in SAFE_METHODS:
            return True

        # Проверяем, что пользователь - автор объекта
        return obj.author == request.user
