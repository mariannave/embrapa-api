import requests
import logging
from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)

SCRAPER_TARGETS = {
    "processamento": {
        "viniferas": "http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_01&opcao=opt_03",
        "americanas-e-hibridas": "http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_02&opcao=opt_03",
        "uva-de-mesa": "http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_03&opcao=opt_03",
        "sem-classificacao": "http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_04&opcao=opt_03",
    },
    "importacao": {
        "vinhos-de-mesa": "http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_01&opcao=opt_05",
        "espumantes": "http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_02&opcao=opt_05",
        "uvas-frescas": "http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_03&opcao=opt_05",
        "uvas-passas": "http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_04&opcao=opt_05",
        "suco-de-uva": "http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_05&opcao=opt_05",
    },
    "exportacao": {
        "vinhos-de-mesa": "http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_01&opcao=opt_06",
        "espumantes": "http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_02&opcao=opt_06",
        "uvas-frescas": "http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_03&opcao=opt_06",
        "suco-de-uva": "http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_04&opcao=opt_06",
    },
    "producao": "http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_02",
    "comercializacao": "http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_04",
}


def get_data(url: str) -> str:
    """Fetch data from a given URL."""
    if not url:
        raise ValueError("URL is required")

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.content.decode("utf-8")
    except requests.RequestException as e:
        logger.error(f"Failed to fetch data from {url}: {str(e)}")
        return None


def parse_str_to_number(str):
    """Convert string with potential thousands separators to integer."""
    try:
        return int(str.replace(".", ""))
    except ValueError:
        return 0


def parse_html_table(year=2023, html_content=None, metadata: dict = {}):
    logger.info("Request html")
    if not html_content:
        return []

    soup = BeautifulSoup(html_content, "html.parser")
    table = soup.find("table", {"class": "tb_base tb_dados"})

    if not table:
        logger.warning("Table not found in HTML content")
        return []

    results = []
    rows = table.find_all("tbody")[0].find_all("tr")

    for row in rows:
        cells = row.find_all("td")

        if cells[0].get("class")[0] == "tb_item":
            item = {
                "item": cells[0].get_text(strip=True),
                "quantity": parse_str_to_number(cells[1].get_text(strip=True)),
                "year": year,
                "sub_items": [],
            }
            item.update(metadata)
            results.append(item)

        if (
            cells[0].get("class")[0] == "tb_subitem"
            and cells[1].get("class")[0] == "tb_subitem"
        ):
            results[-1]["sub_items"].append(
                {
                    "name": cells[0].get_text(strip=True),
                    "quantity": parse_str_to_number(cells[1].get_text(strip=True)),
                }
            )

    return results


def parse_import_export_table(year=2023, html_content=None, metadata: dict = {}):
    logger.info("Request html")
    """Parse import/export specific table data."""
    if not html_content:
        return []

    soup = BeautifulSoup(html_content, "html.parser")
    table = soup.find("table", {"class": "tb_base tb_dados"})

    if not table:
        logger.warning("Table not found in HTML content")
        return []

    results = []
    rows = table.find_all("tbody")[0].find_all("tr")

    for row in rows:
        cells = row.find_all("td")

        item = {
            "country": cells[0].get_text(strip=True),
            "quantity": parse_str_to_number(cells[1].get_text(strip=True)),
            "amount": parse_str_to_number(cells[2].get_text(strip=True)),
            "year": year,
        }
        item.update(metadata)
        results.append(item)

    return results
