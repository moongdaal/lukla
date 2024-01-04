from .base import BaseDatabaseRouter


class AuthenticationRouter(BaseDatabaseRouter):
    """
    A router to control all database operations on models in the
    auth and contenttypes applications.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(
            route_app_labels={
                "auth",
                "contenttypes",
                "session",
                "admin",
                "messages",
                "staticfiles",
            },
            db_name="auth",
            *args,
            **kwargs
        )
