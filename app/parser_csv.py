import csv
from collections import defaultdict
import logging
from decimal import InvalidOperation
from typing import Optional

logger = logging.getLogger(__name__)


def parse_str_to_number(value):
    """Convert string to Int, handling comma-separated decimals."""
    try:
        return int(str(value).replace(",", ""))
    except (InvalidOperation, ValueError):
        return 0


def read_csv_file(path: str, delimiter: str = ";"):
    """Read CSV file and return rows as dictionaries."""
    with open(path, "r", encoding="utf-8") as file:
        return list(csv.DictReader(file, delimiter=delimiter))


def general_csv(
    path: str, year: int = 2023, key: Optional[str] = None, delimiter: str = ";"
):
    """Parse structured CSV with main items and sub-items."""
    logger.info("Request csv")

    reader = read_csv_file(path, delimiter)
    results = []

    for row in reader:
        if row["control"].isupper() or row["control"] == "":
            results.append(
                {
                    "item": row[key].strip(),
                    "quantity": parse_str_to_number(row[f"{year}"]),
                    "year": year,
                    "sub_items": [],
                }
            )
        elif "_" in row["control"] and results:
            results[-1]["sub_items"].append(
                {
                    "name": row[key].strip(),
                    "quantity": parse_str_to_number(row[f"{year}"]),
                }
            )
    return results


def import_export_csv(path: str, year: int = 2023, delimiter: str = ";"):
    """Parse import/export data CSV with duplicate headers."""
    logger.info("Request csv")

    file = open(path, "r")
    reader = csv.reader(file, delimiter=delimiter)
    rows = []
    results = []

    headers = next(reader)
    header_counts = defaultdict(int)
    unique_headers = []

    for header in headers:
        header_counts[header] += 1
        unique_headers.append(
            f"{header}_{header_counts[header]}" if header_counts[header] > 1 else header
        )

    for row in reader:
        rows.append(dict(zip(unique_headers, row)))

    for row in rows:
        item = {
            "country": row["País"],
            "quantity": int(row[f"{year}"]),
            "amount": int(row[f"{year}_2"]),
            "year": year,
        }
        results.append(item)

    return results
