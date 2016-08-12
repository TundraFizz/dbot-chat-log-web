from pyramid.config import Configurator


def main(global_config, **settings):
    config = Configurator(settings=settings)

    config.include("pyramid_jinja2")

    config.add_static_view("static", "static", cache_max_age=3600)

    config.add_route("index", "/")
    config.add_route("readfile", "/readfile")

    config.scan()
    return config.make_wsgi_app()
