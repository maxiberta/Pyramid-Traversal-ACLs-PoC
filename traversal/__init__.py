from pyramid.config import Configurator
from pyramid_beaker import session_factory_from_settings
from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from pyramid.decorator import reify
from pyramid.request import Request
from pyramid.security import unauthenticated_userid
#from traversal.security import groupfinder

class RequestWithUserAttribute(Request):
    @reify
    def user(self):
#        dbconn = self.registry.settings['dbconn']
        userid = unauthenticated_userid(self)
        return userid
#        if userid is not None:
            # this should return None if the user doesn't exist
            # in the database
#            return dbconn['users'].query({'id':userid})
#            return userid

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    authentication_policy = AuthTktAuthenticationPolicy('seekrit')#, callback=groupfinder)
    authorization_policy = ACLAuthorizationPolicy()

    session_factory = session_factory_from_settings(settings)

    config = Configurator(root_factory='traversal.resources.Node',
                          settings=settings,
                          authentication_policy=authentication_policy,
                          authorization_policy=authorization_policy,
                          request_factory=RequestWithUserAttribute,
                          session_factory=session_factory,
                         )

    config.add_route('root', '/')
    config.add_route('login', '/login')
    config.add_route('logout', '/logout')
    config.add_route('monitor_call_route', '/mon/call/*traverse', use_global_views=True)

    config.add_view('traversal.views.view',
                    route_name='root',
                    renderer='traversal:templates/mytemplate.mako',
                    )
    config.add_view('traversal.login.login',
                    route_name='login',
                    renderer='traversal:templates/login.mako',
                    )
    config.add_view('traversal.login.logout',
                    route_name='logout',
                    )
    config.add_view('traversal.views.monitor_call',
                    route_name='monitor_call_route',
                    renderer='traversal:templates/mytemplate.mako',
                    permission='can_monitor_call',
                    )
    config.add_view('traversal.views.view',
                    name='',
                    context='traversal.resources.Node',
                    renderer='traversal:templates/mytemplate.mako',
                    permission='can_view',
                    )
    config.add_view('traversal.views.edit',
                    name='edit',
                    context='traversal.resources.Node',
                    renderer='traversal:templates/mytemplate.mako',
                    permission='can_edit',
                    )

    config.add_static_view('static', 'traversal:static', cache_max_age=3600)

    return config.make_wsgi_app()
