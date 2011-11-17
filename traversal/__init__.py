from pyramid.config import Configurator

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(root_factory='traversal.resources.Root', settings=settings)
    config.add_view('traversal.views.my_view',
                    context='traversal.resources.Root',
                    renderer='traversal:templates/mytemplate.pt')
    config.add_static_view('static', 'traversal:static', cache_max_age=3600)
    return config.make_wsgi_app()
