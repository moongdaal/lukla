from .base import BaseDatabaseRouter


class PrimaryRouter(BaseDatabaseRouter):
    """
    A router to control all database operations on models in the
    auth and contenttypes applications.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(
            route_app_labels={
                "gokyo",
            },
            db_name="operations",
            *args,
            **kwargs
        )
