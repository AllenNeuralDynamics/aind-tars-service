"""Set up fixtures to be used across all test modules."""

import os
from pathlib import Path
import json
import pytest
from fastapi.testclient import TestClient
from requests import Response
from requests_toolbelt.sessions import BaseUrlSession

from aind_tars_service_server.main import app

RESOURCES_DIR = Path(os.path.dirname(os.path.realpath(__file__))) / "resources"


@pytest.fixture()
def mock_get_access_token(mocker):
    """Mock getting a bearer token."""
    mock_get = mocker.patch(
        "aind_tars_service_server..configs.Settings.get_bearer_token"
    )
    mock_get.return_value = ("abc123def456", 1733101170)
    return mock_get


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
    with open(RESOURCES_DIR / "raw_molecules_response.json") as f:
        contents = json.load(f)
    mock_get = mocker.patch(
        "aind_tars_service_server.handler.SessionHandler"
        "._get_raw_molecules_response"
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
        "aind_tars_service_server.handler.SessionHandler" \
        "._get_raw_virus_response"
    )
    mock_response = Response()
    mock_response.status_code = 200
    mock_response._content = json.dumps(contents).encode("utf-8")
    mock_get.return_value = mock_response



@pytest.fixture(scope="session")
def client():
    """Creating a client for testing purposes."""

    with TestClient(app) as c:
        yield c
