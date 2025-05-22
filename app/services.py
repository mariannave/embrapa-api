from app.parser_csv import general_csv, import_export_csv
from app import scraping


def production_data(year: int = 2023):
    html_content = scraping.get_data(
        url=f"{scraping.SCRAPER_TARGETS['producao']}&ano={year}"
    )

    if html_content:
        return scraping.parse_html_table(year=year, html_content=html_content)
    else:
        return general_csv(
            path="/Users/marianna/pos-fiap/projeto/files/producao.csv",
            year=year,
            key="produto",
        )


def commercialization_data(year: int = 2023):
    html_content = scraping.get_data(
        url=f"{scraping.SCRAPER_TARGETS['comercializacao']}&ano={year}"
    )

    if html_content:
        return scraping.parse_html_table(year=year, html_content=html_content)
    else:
        return general_csv(
            path="/Users/marianna/pos-fiap/projeto/files/comercializacao.csv",
            year=year,
            key="Produto",
        )


def processing_data(year: int = 2023, metadata: dict = {}):
    category = metadata["category"]
    html_content = scraping.get_data(
        url=f"{scraping.SCRAPER_TARGETS['processamento'][category]}&ano={year}"
    )
    if html_content:
        return scraping.parse_html_table(year=year, html_content=html_content)
    else:
        return general_csv(
            path=f"/Users/marianna/pos-fiap/projeto/files/processamento-{category}.csv",
            year=year,
            key="cultivar",
            delimiter=(";" if category == "viniferas" else "\t")
        )


def import_data(year: int = 2023, metadata: dict = {}):
    category = metadata["category"]
    html_content = scraping.get_data(
        url=f"{scraping.SCRAPER_TARGETS['importacao'][category]}&ano={year}"
    )

    if html_content:
        return scraping.parse_import_export_table(
            year=year, html_content=html_content, metadata=metadata
        )
    else:
        return import_export_csv(
            path=f"/Users/marianna/pos-fiap/projeto/files/importacao-{category}.csv",
            year=year,
            delimiter=(";" if category == "suco-de-uva" else "\t"),
        )


def export_data(year: int = 2023, metadata: dict = {}):
    category = metadata["category"]
    html_content = scraping.get_data(
        url=f"{scraping.SCRAPER_TARGETS['exportacao'][category]}&ano={year}"
    )

    if html_content:
        return scraping.parse_import_export_table(
            year=year, html_content=html_content, metadata=metadata
        )
    else:
        return import_export_csv(
            path=f"/Users/marianna/pos-fiap/projeto/files/exportacao-{category}.csv",
            year=year,
            delimiter="\t",
        )
