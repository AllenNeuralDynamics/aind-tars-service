"""Module for settings to connect to TARS backend"""

from typing import Optional
from urllib.parse import urljoin

from pydantic import Field, HttpUrl, RedisDsn, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Settings needed to connect to TARS."""

    # noinspection SpellCheckingInspection
    model_config = SettingsConfigDict(env_prefix="TARS_")
    tenant_id: str = Field(..., description="Azure tenant id.")
    client_id: str = Field(
        ..., description="Client ID of the service account accessing resource."
    )
    client_secret: SecretStr = Field(
        ..., description="Secret used to access the account."
    )
    scope: str = Field(..., description="Scope")
    resource: HttpUrl = Field(..., description="Resource")
    redis_url: Optional[RedisDsn] = Field(default=None)

    @property
    def viral_prep_lots_url(self) -> HttpUrl:
        """URL for ViralPrepLots"""
        return HttpUrl.build(
            scheme=self.resource.scheme,
            host=self.resource.host,
            path=urljoin(
                f"{self.resource.path.lstrip('/')}/", "api/v1/ViralPrepLots"
            ).lstrip("/"),
        )

    @property
    def viruses_url(self) -> HttpUrl:
        """URL for Viruses"""
        return HttpUrl.build(
            scheme=self.resource.scheme,
            host=self.resource.host,
            path=urljoin(
                f"{self.resource.path.lstrip('/')}/", "api/v1/Viruses"
            ).lstrip("/"),
        )

    @property
    def molecules_url(self) -> HttpUrl:
        """URL for Molecules"""
        return HttpUrl.build(
            scheme=self.resource.scheme,
            host=self.resource.host,
            path=urljoin(
                f"{self.resource.path.lstrip('/')}/", "api/v1/Molecules"
            ).lstrip("/"),
        )


def get_settings() -> Settings:
    """Utility method to return a settings object."""
    return Settings()
