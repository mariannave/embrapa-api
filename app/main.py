from fastapi import FastAPI
from app import routers
import logging

description = """
    This API searches for data on the website http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_01 belonging to Embrapa - The Brazilian Agricultural Research Corporation.
"""
app = FastAPI(
    title="Embrapa API",
    version="0.1.0",
    description=description,
    openapi_url="/api/v1/openapi.json",
)
app.include_router(routers.router)

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s %(levelname)-5.5s [%(name)s] %(message)s"
)
