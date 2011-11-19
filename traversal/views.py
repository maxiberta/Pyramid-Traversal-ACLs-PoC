import pyramid

def my_view(request):
    print __name__
    userid = pyramid.security.authenticated_userid(request)
    return {'project':'traversal', 'userid':userid}
