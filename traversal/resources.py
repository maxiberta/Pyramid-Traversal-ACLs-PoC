from pyramid.security import Allow
from pyramid.security import Everyone

class RootFactory(dict):

    __acl__ = [ (Allow, Everyone, 'view'),
                (Allow, 'group:editors', 'edit') ]

    def __init__(self, request):
        print __name__
        self.request = request
        self['edit'] = 'edit'
