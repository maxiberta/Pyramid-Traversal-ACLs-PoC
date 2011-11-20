from pyramid.security import authenticated_userid

def view(request):
    print __name__ + '.view'
    userid = authenticated_userid(request)
    return {'project':'traversal', 'userid':userid}

def edit(request):
    print __name__ + '.edit'
    userid = authenticated_userid(request)
    return {'project':'traversal', 'userid':userid}
