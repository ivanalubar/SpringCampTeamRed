def user_permission(user):
    permissions = ''
    for group in user.groups.all():
        if group.name == 'profesor':
            permissions = 'profesor'
        if group.name == 'student' and permissions != 'profesor':
            permissions = 'student'

    return permissions


def request_permission(request):
    if request.user.is_authenticated:
        return user_permission(request.user)
    else:
        return None