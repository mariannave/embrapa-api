from datetime import timedelta
from typing import Literal, Annotated
from fastapi import APIRouter, Depends, HTTPException, Query, status, Path
from app import services
from fastapi.security import OAuth2PasswordRequestForm
import os

from app.auth import (
    authenticate_user,
    create_access_token,
    fake_users_db,
    get_current_active_user,
)
from app.models import Token


api_router = APIRouter(
    prefix="/v1",
    responses={404: {"description": "Not found"}},
    dependencies=[Depends(get_current_active_user)],
)
auth_router = APIRouter(prefix="/auth", responses={404: {"description": "Not found"}})


@auth_router.post("/token")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
) -> Token:
    user = authenticate_user(fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(
        minutes=float(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))
    )
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")


@api_router.get("/production", summary="Return production data")
async def production(
    year: int = Query(
        2023,
        ge=1970,
        le=2023,
        description="Year of production data (must be between 1970 and 2023)",
    )
):
    """
    Retrieve wines, juices, and derivates production statistics in Rio Grande
    do Sul

    Parameters:
    - **year**: Year of production data (defaults to 2023)

    Returns:
    - Production volume and type statistics from Embrapa's database
    """
    return services.production_data(year)


@api_router.get("/commercialization", summary="Return commercialization data")
async def commercialization(
    year: int = Query(
        2023,
        ge=1970,
        le=2023,
        description="Year of commercialization data (must be between 1970 and 2023)",
    )
):
    """
    Retrieve wines, juices, and derivatives commercialization statistics for Rio Grande do Sul market

    Parameters:
    - **year**: Year of commercialization data (defaults to 2023)

    Returns:
    - Commercialization volume and type statistics from Embrapa's database
    """
    return services.commercialization_data(year)


@api_router.get("/processing/{category}", summary="Return processing data")
async def processing(
    category: Literal[
        "viniferas", "americanas-e-hibridas", "uva-de-mesa", "sem-classificacao"
    ],
    year: int = Query(
        2023,
        ge=1970,
        le=2023,
        description="Year of processing data (must be between 1970 and 2023)",
    ),
):
    """
    Get data about grape processing categorized by type

    Parameters:
    - **category**: Type of grape being processed (path parameter with predefined options)
    - **year**: Year of the data in question (default: 2023)
    """
    return services.processing_data(year, metadata={"category": category})


@api_router.get("/import/{category}", summary="Return import data by category")
async def importation(
    category: Literal[
        "vinhos-de-mesa", "espumantes", "uvas-frescas", "uvas-passas", "suco-de-uva"
    ],
    year: int = Query(
        2024,
        ge=1970,
        le=2024,
        description="Year of importation data (must be between 1970 and 2023)",
    ),
):
    """
    Retrieve data about imported grape derivatives products

    Parameters:
    - **category**: Import category (one of five predefined options)
    - **year**: Year of data collection (default: 2024)
    """
    return services.import_data(year, metadata={"category": category})


@api_router.get("/export/{category}", summary="Return export data by category")
async def export(
    category: Literal["vinhos-de-mesa", "espumantes", "uvas-frescas", "suco-de-uva"],
    year: int = Query(
        2024,
        ge=1970,
        le=2024,
        description="Year of importation data (must be between 1970 and 2023)",
    ),
):
    """
    Retrieve data about exported grape derivatives products

    Parameters:
    - **category**: Export type subcategory (four available options)
    - **year**: Year of export data (default: 2024)
    """
    return services.export_data(year, metadata={"category": category})
