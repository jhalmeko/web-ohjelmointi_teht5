from services.service_factory import auth_service_factory


def init_service(name):
    def decorator(route_handler_func):
        def wrapper(conn, *args, **kwargs):
            if name == 'auth_service':
                service = auth_service_factory(conn)
                return route_handler_func(service, *args, **kwargs)
        return wrapper
    return decorator