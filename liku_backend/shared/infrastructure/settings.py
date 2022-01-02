from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    birthday_repository_type: str = Field(..., description="mongo or atlas")
    birthday_repository_host: str = Field("host", description="url to access the db")
    birthday_repository_port: int = Field(17420, description="port to access the db")
    birthday_repository_user: str = Field("user", description="user to access the db")
    birthday_repository_password: str = Field(..., description="password to access the db")
    birthday_repository_database_name: str = Field(..., description="name of the db to access")
    gift_repository_type: str = Field(..., description="mongo or atlas")
    gift_repository_host: str = Field("host", description="url to access the db")
    gift_repository_port: int = Field(17420, description="port to access the db")
    gift_repository_user: str = Field("user", description="user to access the db")
    gift_repository_password: str = Field(..., description="password to access the db")
    gift_repository_database_name: str = Field(..., description="name of the db to access")
