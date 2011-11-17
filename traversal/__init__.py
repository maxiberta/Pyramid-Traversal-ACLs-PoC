from pyramid.config import Configurator
from pyramid_beaker import session_factory_from_settings
from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    authentication_policy = AuthTktAuthenticationPolicy('seekrit')
    authorization_policy = ACLAuthorizationPolicy()

    session_factory = session_factory_from_settings(settings)

    config = Configurator(root_factory='traversal.resources.RootFactory',
                                settings=settings,
                                authentication_policy=authentication_policy,
                                authorization_policy=authorization_policy,
                                session_factory=session_factory,
    )

    config.add_route('login', '/login')
    config.add_view('traversal.login.login',
                    route_name='login',
#                    context='pyramid.httpexceptions.HTTPForbidden',
                    renderer='traversal:templates/login.pt')

    config.add_route('logout', '/logout')
    config.add_view('traversal.login.logout', route_name='logout')

    config.add_view('traversal.views.my_view',
                    context='traversal.resources.RootFactory',
                    renderer='traversal:templates/mytemplate.pt',
                    permission='edit')

    config.add_static_view('static', 'traversal:static', cache_max_age=3600)

    return config.make_wsgi_app()
