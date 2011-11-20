from pyramid.security import Allow, Deny
from pyramid.security import Everyone
from pyramid.security import has_permission
from pyramid.location import lineage

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
    'editor': { 'Allow': {  'Argentina': ['view'],
                            'Capital': ['edit', 'delete'],
                        },
                'Deny': {   'Avellaneda': ['view'],
                            'Palermo': ['view', 'edit'],
                        },
            }
}

class Node(object):
    def __init__(self, request, name='', parent=None, children=HIERARCHY):
        self.request = request
        self.__name__ = name
        self.__parent__ = parent
        self._children = children

    def __getitem__(self, key):
        if key in self._children:
            return Node(self.request, key, self, self._children[key])
        raise KeyError

    def __repr__(self):
        return self.__name__ or u'root'

    def lineage(self):
        return reversed(list(lineage(self)))

    def children(self):
        return [Node(self.request, key, self, self._children[key]) for key in self._children]

    @property
    def __acl__(self):
        userid = self.request.user
        permissions = []
        try:
            permissions += [(Deny, userid, permission) for permission in ACLs[userid]['Deny'][self.__name__]]
        except KeyError:
            pass
        try:
            permissions += [(Allow, userid, permission) for permission in ACLs[userid]['Allow'][self.__name__]]
        except KeyError:
            pass
        return permissions

    def allows(self, permission):
        return has_permission(permission, self, self.request)
