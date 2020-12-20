from pydantic import BaseSettings, PostgresDsn


class Settings(BaseSettings):
    postgres_dsn: PostgresDsn

    # This part sets up the mapping between the variable name and the environment variable.
    # In this example, the value of postgres_dsn will be pulled from the environment variable "POSTGRES_DSN"
    #
    # This makes it easy to change the database we connect to by simply changing the environment variable
    # and restarting our application.
    class Config:
        fields = {
            'postgres_dsn': {
                'env': 'POSTGRES_DSN'  # 'postgres://<user>:<pass>@<host>>:<port>>/<dbname>'
            }
        }


settings = Settings()
