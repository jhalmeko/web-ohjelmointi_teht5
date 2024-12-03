import os

from repositories.repository_factory import users_repository_factory


def init_repository(repo_name):
    def decorator(route_handler_func):
        def wrapper(con, *args, **kwargs):
            repo = None
            if repo_name == 'users_repo':
                repo = users_repository_factory(con)

            return route_handler_func(repo, *args, **kwargs)
        return wrapper
    return decorator