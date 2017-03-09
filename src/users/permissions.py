# -*- coding: utf-8 -*-
from rest_framework.permissions import BasePermission


class UserPermission(BasePermission):

    def has_permission(self, request, view):
        """
        Define si un usuario puede usar o no el endpoint que quiere utilizar
        :param request: HttpRequest
        :param view: UsersAPI/UserDetailAPI
        :return: True si puede, False si no puede
        """
        from users.api import UserDetailAPI

        # cualquiera puede crear un usuario (POST)
        if request.method == "POST":
            return True

        # si esta autenticado y quiere hacer algo sobre el detalle o es superusuario y quiere hacer algo sobre el listado
        if request.user.is_authenticated() and (request.user.is_superuser or isinstance(view, UserDetailAPI)):
            return True

        return False

    def has_object_permission(self, request, view, obj):
        """
        Define si el usuario puede realizar la acción sobre el objeto que quiere realizarla
        :param request: HttpRequest
        :param view: UsersAPI/UserDetailAPI
        :param obj: User
        :return: True si puede, False si no puede
        """
        # si es admin o si es él mismo, le dejamos
        return request.user.is_superuser or request.user == obj
