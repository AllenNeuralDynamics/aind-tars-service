"""Module to handle endpoint responses"""

from typing import List

from azure.core.credentials import AccessToken
from azure.identity import ClientSecretCredential
from fastapi import APIRouter, Path, Query, status
from fastapi_cache.decorator import cache
from httpx import AsyncClient

from aind_tars_service_server.configs import settings
from aind_tars_service_server.handler import SessionHandler
from aind_tars_service_server.models import (
    HealthCheck,
    MoleculeData,
    PrepLotData,
    VirusData,
)

router = APIRouter()


@router.get(
    "/healthcheck",
    tags=["healthcheck"],
    summary="Perform a Health Check",
    response_description="Return HTTP Status Code 200 (OK)",
    status_code=status.HTTP_200_OK,
    response_model=HealthCheck,
)
async def get_health() -> HealthCheck:
    """
    ## Endpoint to perform a healthcheck on.

    Returns:
        HealthCheck: Returns a JSON response with the health status
    """
    return HealthCheck()


@cache(expire=3500)
async def get_access_token() -> str:
    """
    Get access token from either Azure or cache. Token is valid for 60 minutes.
    We set cache ttl to 3500 seconds.

    Returns
    -------
    str

    """
    credentials: AccessToken = ClientSecretCredential(
        tenant_id=settings.tenant_id,
        client_id=settings.client_id,
        client_secret=settings.client_secret.get_secret_value(),
    ).get_token(settings.scope)
    return credentials.token


@router.get(
    "/viral_prep_lots/{lot}",
    response_model=List[PrepLotData],
)
async def get_viral_prep_lots(
    lot: str = Path(
        ...,
        openapi_examples={
            "default": {
                "summary": "A sample prep lot ID",
                "description": "Example prep lot ID for TARS",
                "value": "VT3214g",
            }
        },
    ),
    page_size: int = Query(
        1,
        le=50,
        alias="page_size",
        description="Number of items to return in a single page.",
        openapi_examples={
            "default": {
                "summary": "A sample page size",
                "description": "Example page size for TARS",
                "value": 1,
            }
        },
    ),
    limit: int = Query(
        1,
        alias="limit",
        description="Limit number of items returned. Set to 0 to return all.",
        openapi_examples={
            "default": {
                "summary": "A sample limit",
                "description": "Example limit for TARS",
                "value": 1,
            }
        },
    ),
):
    """
    ## TARS Endpoint to retrieve viral prep lot data.
    Retrieves viral prep lot information from TARS for a prep_lot_id.
    """
    bearer_token = await get_access_token()
    headers = {
        "Authorization": f"Bearer {bearer_token}",
        "Content-Type": "application/json",
    }
    query_params = {
        "pageSize": str(page_size),
        "order": "1",
        "orderBy": "id",
        "searchFields": "lot",
        "search": lot.strip(),
    }
    async with AsyncClient(headers=headers) as client:
        handler = SessionHandler(client=client)
        raw_prep_lot_data = await handler.get_data(
            url=settings.viral_prep_lots_url.unicode_string(),
            params=query_params,
            limit=limit,
        )
    prep_lot_data = [PrepLotData.model_validate(r) for r in raw_prep_lot_data]
    return prep_lot_data


@router.get(
    "/molecules/{name}",
    response_model=List[MoleculeData],
)
async def get_molecules(
    name: str = Path(
        ...,
        openapi_examples={
            "default": {
                "summary": "A sample molecule name",
                "description": "Example molecule name for TARS",
                "value": "AiP20611",
            }
        },
    ),
    page_size: int = Query(
        1,
        le=50,
        alias="page_size",
        description="Number of items to return in a single page.",
        openapi_examples={
            "default": {
                "summary": "A sample page size",
                "description": "Example page size for TARS",
                "value": 1,
            }
        },
    ),
    limit: int = Query(
        1,
        alias="limit",
        description="Limit number of items returned. Set to 0 to return all.",
        openapi_examples={
            "default": {
                "summary": "A sample limit",
                "description": "Example limit for TARS",
                "value": 1,
            }
        },
    ),
):
    """
    ## TARS Endpoint to molecule data.
    """
    bearer_token = await get_access_token()
    headers = {
        "Authorization": f"Bearer {bearer_token}",
        "Content-Type": "application/json",
    }
    query_params = {
        "pageSize": str(page_size),
        "order": "1",
        "orderBy": "id",
        "searchFields": "name",
        "search": name.strip(),
    }
    async with AsyncClient(headers=headers) as client:
        handler = SessionHandler(client=client)
        raw_molecule_data = await handler.get_data(
            url=settings.molecules_url.unicode_string(),
            params=query_params,
            limit=limit,
        )
    molecule_data = [MoleculeData.model_validate(r) for r in raw_molecule_data]
    return molecule_data


@router.get(
    "/viruses/{name}",
    response_model=List[VirusData],
)
async def get_viruses(
    name: str = Path(
        ...,
        openapi_examples={
            "default": {
                "summary": "A sample virus name",
                "description": "Example virus name for TARS",
                "value": "VIR300002_PHPeB",
            }
        },
    ),
    page_size: int = Query(
        1,
        le=50,
        alias="page_size",
        description="Number of items to return in a single page.",
        openapi_examples={
            "default": {
                "summary": "A sample page size",
                "description": "Example page size for TARS",
                "value": 1,
            }
        },
    ),
    limit: int = Query(
        1,
        alias="limit",
        description="Limit number of items returned. Set to 0 to return all.",
        openapi_examples={
            "default": {
                "summary": "A sample limit",
                "description": "Example limit for TARS",
                "value": 1,
            }
        },
    ),
):
    """
    ## TARS Endpoint to virus data.
    """
    bearer_token = await get_access_token()
    headers = {
        "Authorization": f"Bearer {bearer_token}",
        "Content-Type": "application/json",
    }
    query_params = {
        "pageSize": str(
            page_size
        ),  # Also fixed this - should be "pageSize" not "page_size"
        "order": "1",
        "orderBy": "id",
        "searchFields": "aliases.name",
        "search": name.strip(),
    }
    async with AsyncClient(headers=headers) as client:
        handler = SessionHandler(client=client)
        raw_virus_data = await handler.get_data(
            url=settings.viruses_url.unicode_string(),
            params=query_params,
            limit=limit,
        )
    virus_data = [VirusData.model_validate(r) for r in raw_virus_data]
    return virus_data
