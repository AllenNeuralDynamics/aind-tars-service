"""Module for settings to connect to TARS backend"""

from typing import Optional

from pydantic import Field, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Settings needed to connect to LabTracks Database"""

    # noinspection SpellCheckingInspection
    model_config = SettingsConfigDict(env_prefix="TARS_")
    tenant_id: str = Field(
        ..., description="The ID of the AllenInstituteB2C Azure tenant."
    )
    client_id: str = Field(
        ..., description="Client ID of the service account accessing resource."
    )
    client_secret: SecretStr = Field(
        ..., description="Secret used to access the account."
    )
    scope: str = Field(..., description="Scope")
    resource: str = Field(..., description="Resource")
    redis_url: Optional[str] = Field(default=None)


def get_settings() -> Settings:
    """Utility method to return a settings object."""
    return Settings()
