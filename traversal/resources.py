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
    'editor': { 'Allow': {  'Argentina': ['can_view'],
                            'Capital': ['can_edit'],
                            'Belgrano': ['can_monitor_call'],
                        },
                'Deny': {   'Avellaneda': ['can_view'],
                            'Palermo': ['can_view', 'can_edit'],
                        },
            }
}

class Node(object):
    def __init__(self, request, name='', parent=None, children=HIERARCHY):
        self.request = request
        self.__name__ = name
        self.__parent__ = parent
        self._children = children
        self.__acl__ = self.get_acls()

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

    def get_acls(self):
        userid = self.request.user
        acls = []
        try:
            acls += [(Deny, userid, permission) for permission in ACLs[userid]['Deny'][self.__name__]]
        except KeyError:
            pass
        try:
            acls += [(Allow, userid, permission) for permission in ACLs[userid]['Allow'][self.__name__]]
        except KeyError:
            pass
        return acls

    def has_permission(self, permission):
        return has_permission(permission, self, self.request)

    def url(self):
        if self.request.matched_route:
            return self.request.route_url(self.request.matched_route.name, traverse=self.request.traversed)
        else:
            return self.request.resource_url(self.request.context)
