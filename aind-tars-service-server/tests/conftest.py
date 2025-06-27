"""Set up fixtures to be used across all test modules."""

import json
import os
from pathlib import Path
from typing import Any, Generator
from unittest.mock import patch

import pytest
from fastapi.testclient import TestClient
from requests import Response

from aind_tars_service_server.configs import Settings

RESOURCES_DIR = Path(os.path.dirname(os.path.realpath(__file__))) / "resources"

patch(
    "fastapi_cache.decorator.cache", lambda *args, **kwargs: lambda f: f
).start()


@pytest.fixture()
def mock_get_raw_prep_lot_response(mocker):
    """Mock raw prep_lot response"""
    with open(RESOURCES_DIR / "raw_prep_lot_response.json") as f:
        contents = json.load(f)
    mock_get = mocker.patch(
        "aind_tars_service_server.handler.SessionHandler"
        "._get_raw_prep_lot_response"
    )
    mock_response = Response()
    mock_response.status_code = 200
    mock_response._content = json.dumps(contents).encode("utf-8")
    mock_get.return_value = mock_response


@pytest.fixture()
def mock_get_raw_molecule_response(mocker):
    """Mock raw molecule response"""
    with open(RESOURCES_DIR / "raw_molecule_response.json") as f:
        contents = json.load(f)
    mock_get = mocker.patch(
        "aind_tars_service_server.handler.SessionHandler"
        "._get_raw_molecule_response"
    )
    mock_response = Response()
    mock_response.status_code = 200
    mock_response._content = json.dumps(contents).encode("utf-8")
    mock_get.return_value = mock_response


@pytest.fixture()
def mock_get_raw_virus_response(mocker):
    """Mock raw virus response"""
    with open(RESOURCES_DIR / "raw_virus_response.json") as f:
        contents = json.load(f)
    mock_get = mocker.patch(
        "aind_tars_service_server.handler.SessionHandler"
        "._get_raw_virus_response"
    )
    mock_response = Response()
    mock_response.status_code = 200
    mock_response._content = json.dumps(contents).encode("utf-8")
    mock_get.return_value = mock_response


@pytest.fixture(scope="session")
def client() -> Generator[TestClient, Any, None]:
    """Creating a client for testing purposes."""

    # Import moved to be able to mock cache
    from aind_tars_service_server.main import app

    with TestClient(app) as c:
        yield c


@pytest.fixture(scope="function")
def client_with_redis() -> Generator[TestClient, Any, None]:
    """Creating a client when settings have a redis_url. Only used in one test
    to verify the lifespan method in main is called correctly."""

    # Import moved to be able to mock cache
    from aind_tars_service_server.main import app

    settings = Settings()
    settings_with_redis = settings.model_copy(
        update={"redis_url": "redis"}, deep=True
    )
    with (
        patch(
            "aind_tars_service_server.main.get_settings",
            return_value=settings_with_redis,
        ),
        patch("aind_tars_service_server.main.from_url", return_value=None),
        patch(
            "aind_tars_service_server.main.RedisBackend",
            return_value=None,
        ),
    ):
        with TestClient(app) as c:
            yield c
