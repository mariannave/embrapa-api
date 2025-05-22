from typing import Literal
from fastapi import APIRouter
from app import services


router = APIRouter(
    prefix="/v1",
    responses={404: {"description": "Not found"}},
)


@router.get("/production", summary="Return production data")
async def production(year: int = 2023):
    """
    Retrieve wines, juices, and derivates production statistics in Rio Grande
    do Sul

    Parameters:
    - **year**: Year of production data (defaults to 2023)

    Returns:
    - Production volume and type statistics from Embrapa's database
    """
    return services.production_data(year)


@router.get("/commercialization", summary="Return commercialization data")
async def commercialization(year: int = 2023):
    """
    Retrieve wines, juices, and derivatives commercialization statistics for Rio Grande do Sul market

    Parameters:
    - **year**: Year of commercialization data (defaults to 2023)

    Returns:
    - Commercialization volume and type statistics from Embrapa's database
    """
    return services.commercialization_data(year)


@router.get("/processing/{category}", summary="Return processing data")
async def processing(
    category: Literal[
        "viniferas", "americanas-e-hibridas", "uva-de-mesa", "sem-classificacao"
    ],
    year: int = 2023,
):
    """
    Get data about grape processing categorized by type

    Parameters:
    - **category**: Type of grape being processed (path parameter with predefined options)
    - **year**: Year of the data in question (default: 2023)
    """
    return services.processing_data(year, metadata={"category": category})


@router.get("/import/{category}", summary="Return import data by category")
async def importation(
    category: Literal[
        "vinhos-de-mesa", "espumantes", "uvas-frescas", "uvas-passas", "suco-de-uva"
    ],
    year: int = 2024,
):
    """
    Retrieve data about imported grape derivatives products

    Parameters:
    - **category**: Import category (one of five predefined options)
    - **year**: Year of data collection (default: 2024)
    """
    return services.import_data(year, metadata={"category": category})


@router.get("/export/{category}", summary="Return export data by category")
async def export(
    category: Literal["vinhos-de-mesa", "espumantes", "uvas-frescas", "suco-de-uva"],
    year: int = 2024,
):
    """
    Retrieve data about exported grape derivatives products

    Parameters:
    - **category**: Export type subcategory (four available options)
    - **year**: Year of export data (default: 2024)
    """
    return services.export_data(year, metadata={"category": category})
