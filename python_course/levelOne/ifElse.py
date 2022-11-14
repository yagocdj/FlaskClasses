username = 'Admin'
has_permission = True

if username == 'Admin' and has_permission:
    print('Full access.')
elif username == 'Admin' and not has_permission:
    print('Admin access only.')
else:
    print('NO permission.')

if 1 < 2:
    print('Yep!')