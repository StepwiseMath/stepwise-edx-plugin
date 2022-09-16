def is_faculty(user):
    if user.is_staff or user.is_superuser:
        return True
    return False
