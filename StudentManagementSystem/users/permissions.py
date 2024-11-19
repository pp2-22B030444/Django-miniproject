from rest_framework import permissions


class IsStudent(permissions.BasePermission):
    """
    Custom permission to allow students to access their own records only.
    """
    def has_object_permission(self, request, view, obj):
        # Ensure the student can only access their own data
        # Assuming `obj` has a field linking to the user, like `obj.user`
        return request.user.is_authenticated and request.user.is_student() and obj.user == request.user


class IsTeacher(permissions.BasePermission):
    """
    Custom permission to allow teachers to access and modify relevant data.
    """
    def has_permission(self, request, view):
        # Allow access only if the user is authenticated and has a TEACHER role
        return request.user.is_authenticated and request.user.is_teacher()

    def has_object_permission(self, request, view, obj):
        # Teachers might have access to specific objects if needed
        # Adjust based on your object-level logic
        return request.user.is_teacher()


class IsAdmin(permissions.BasePermission):
    """
    Custom permission to allow admins to access all data.
    """
    def has_permission(self, request, view):
        # Allow access only if the user is authenticated and has an ADMIN role
        return request.user.is_authenticated and request.user.is_admin()

    def has_object_permission(self, request, view, obj):
        # Admins can access any object
        return request.user.is_admin()


class IsAuthenticated(permissions.BasePermission):
    """
    General permission to allow only authenticated users access.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated


class IsStudentOrTeacher(permissions.BasePermission):
    """
    Custom permission to allow both students and teachers access to specific data.
    """
    def has_permission(self, request, view):
        # Allow access if the user is either a student or a teacher
        return request.user.is_authenticated and (request.user.is_student() or request.user.is_teacher())

    def has_object_permission(self, request, view, obj):
        # Adjust based on specific object-level logic
        return request.user.is_student() or request.user.is_teacher()