import reflex as rx

class ReflextestpageConfig(rx.Config):
    pass

config = ReflextestpageConfig(
    app_name="reflex_test_page",
    db_url="sqlite:///reflex.db",
    env=rx.Env.DEV,
)