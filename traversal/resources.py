from pyramid.security import Allow
from pyramid.security import Everyone
from pyramid.security import authenticated_userid

HIERARCHY = {
    'Argentina': {
        'BsAs': {
            'Capital': {
                'Palermo': {},
                'Belgrano': {},
            },
            'Avellaneda': {
                'Lanus': {},
            },
        },
        'Cordoba': {},
    },
    'Colombia': {
        'Location1': {},
        'Location2': {},
    },

}

ACLs = {
    'editor': { 'Capital': ('edit', 'delete'),
                'Lanus':   ('edit',)},
}

class Node(object):
    def __init__(self, request, name='', parent=None, children=HIERARCHY):
        print __name__ + '.init'
        self.request = request
        self.__name__ = name
        self.__parent__ = parent
        self.children = children

    def __getitem__(self, key):
        print __name__ + '.__getitem__'
        if key in self.children:
            return Node(self.request, key, self, self.children[key])
        raise KeyError

    def __repr__(self):
        return self.__name__ or u'root'

    @property
    def __acl__(self):
        print __name__ + '.__acl__'
        userid = authenticated_userid(self.request)
        permissions = []
        try:
            permissions = [('Allow', userid, permission) for permission in ACLs[userid][self.__name__]]
        except KeyError:
            pass
        return [(Allow, Everyone, 'view')] + permissions

