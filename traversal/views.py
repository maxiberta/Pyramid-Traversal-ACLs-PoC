from inspect import stack

def func_name():
    return '.'.join((__name__ ,stack()[1][3]))

def view(request):
    return {'project':'traversal', 'view': func_name() }

def edit(request):
    return {'project':'traversal', 'view': func_name() }

def monitor_call(request):
    return {'project':'traversal', 'view': func_name() }
