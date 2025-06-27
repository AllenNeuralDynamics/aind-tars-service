"""Module to handle endpoint responses"""

from typing import List

from azure.core.credentials import AccessToken
from azure.identity import ClientSecretCredential
from fastapi import APIRouter, Depends, HTTPException, Path, status
from fastapi_cache.decorator import cache
from requests import Session

from aind_tars_service_server.configs import Settings, get_settings
from aind_tars_service_server.handler import SessionHandler
from aind_tars_service_server.models import (
    HealthCheck,
    MoleculeData,
    PrepLotData,
    Virus,
)
from aind_tars_service_server.session import get_session

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
async def get_access_token(settings: Settings) -> str:
    """
    Get access token from either Azure or cache. Token is valid for 60 minutes.
    We set cache ttl to 3500 seconds.
    Parameters
    ----------
    settings : Settings

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
    "/viral_prep_lot/{prep_lot_id}",
    response_model=List[PrepLotData],
)
async def get_viral_prep_lot(
    prep_lot_id: str = Path(..., examples=["VT3214g"]),
    session: Session = Depends(get_session),
    settings: Settings = Depends(get_settings),
):
    """
    ## TARS Endpoint to retrieve viral prep lot data.
    Retrieves viral prep lot information from TARS for a prep_lot_id.
    """
    bearer_token = await get_access_token(settings=settings)
    handler = SessionHandler(
        session=session, bearer_token=bearer_token, settings=settings
    )
    prep_lot_data = handler.get_prep_lot_data(prep_lot_id=prep_lot_id)
    if len(prep_lot_data) == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Prep lot with ID {prep_lot_id} not found",
        )
    return prep_lot_data


@router.get(
    "/molecule/{plasmid_name}",
    response_model=List[MoleculeData],
)
async def get_molecule_data(
    plasmid_name: str = Path(..., examples=["AiP20611"]),
    session: Session = Depends(get_session),
    settings: Settings = Depends(get_settings),
):
    """
    ## TARS Endpoint to retrieve molecule data.
    Retrieves molecule data information from TARS for a prep_lot_id.
    """
    bearer_token = await get_access_token(settings=settings)
    handler = SessionHandler(
        session=session, bearer_token=bearer_token, settings=settings
    )
    molecule_data = handler.get_molecule_data(plasmid_name=plasmid_name)
    if len(molecule_data) == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Molecule data for {plasmid_name} not found",
        )
    return molecule_data


@router.get(
    "/virus/{virus_name}",
    response_model=List[Virus],
)
async def get_virus_data(
    virus_name: str = Path(..., examples=["VIR300002_PHPeB"]),
    session: Session = Depends(get_session),
    settings: Settings = Depends(get_settings),
):
    """
    ## TARS Endpoint to retrieve virus data.
    Retrieves virus data information from TARS for a virus_name.
    """
    bearer_token = await get_access_token(settings=settings)
    handler = SessionHandler(
        session=session, bearer_token=bearer_token, settings=settings
    )
    virus_data = handler.get_virus_data(virus_name=virus_name)
    if len(virus_data) == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Virus data for {virus_name} not found",
        )
    return virus_data
