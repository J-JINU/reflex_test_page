import reflex as rx

class ReflextestpageConfig(rx.Config):
    pass

config = rx.Config(
    frontend_port=3000,
    app_name = "reflex_test_page",
    db_config = rx.DBConfig(
        engine = "postgresql+psycopg2",
        username = "test_",
        password = "your-db-password",
        host = "localhost",
        port = 5432,
        database = "reflexdb"
    )
)

# config = ReflextestpageConfig(
#     app_name="reflex_test_page",
#     db_url="sqlite:///reflex.db",
#     env=rx.Env.DEV,
# )