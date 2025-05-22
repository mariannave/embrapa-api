from app import scraping


def test_parser_str_to_number_returns_1_when_argument_is_1():
    assert scraping.parse_str_to_number("1") == 1


def test_parser_str_to_number_returns_1000_when_argument_is_1_000():
    assert scraping.parse_str_to_number("1.000") == 1000


def test_parser_str_to_number_returns_0_when_argument_is_invalid():
    assert scraping.parse_str_to_number("-") == 0


class TestGeneralParser:
    def test_return_empty_list_when_html_content_is_empty(self):
        assert scraping.parse_html_table(html_content="") == []

    def test_return_item_and_subitem(self):
        with open("tests/fixtures/general_parser_item_subitem.html", "r") as f:
            expected = [
                {
                    "item": "TINTAS",
                    "quantity": 502666358,
                    "sub_items": [
                        {"name": "Bacarina", "quantity": 0},
                        {"name": "Bailey", "quantity": 587066},
                    ],
                    "year": 2023,
                }
            ]
            assert (
                scraping.parse_html_table(html_content=f.read())
                == expected
            )

    def test_return_item(self):
        with open("tests/fixtures/general_parser_item.html", "r") as f:
            expected = [
                {
                    "item": "TINTAS",
                    "quantity": 502666358,
                    "sub_items": [],
                    "year": 2023,
                }
            ]
            assert (
                scraping.parse_html_table(html_content=f.read())
                == expected
            )


class TestImportExportParser:
    def test_return_empty_list_when_html_content_is_empty(self):
        assert scraping.parse_import_export_table(html_content="") == []

    def test_return_items(self):
        with open("tests/fixtures/import_export_table.html", "r") as f:
            expected = [
                {"country": "Afeganistão", "quantity": 0, "amount": 0, "year": 2023},
                {
                    "country": "África do Sul",
                    "quantity": 103,
                    "amount": 1783,
                    "year": 2023,
                },
                {
                    "country": "Alemanha, República Democrática",
                    "quantity": 6666,
                    "amount": 48095,
                    "year": 2023,
                },
            ]
            assert scraping.parse_import_export_table(html_content=f.read()) == expected

    def test_return_metadata(self):
        with open("tests/fixtures/import_export_table.html", "r") as f:
            expected = [
                {
                    "country": "Afeganistão",
                    "quantity": 0,
                    "amount": 0,
                    "year": 2023,
                    "product": "Vinhos de mesa",
                },
                {
                    "country": "África do Sul",
                    "quantity": 103,
                    "amount": 1783,
                    "year": 2023,
                    "product": "Vinhos de mesa",
                },
                {
                    "country": "Alemanha, República Democrática",
                    "quantity": 6666,
                    "amount": 48095,
                    "year": 2023,
                    "product": "Vinhos de mesa",
                },
            ]
            assert (
                scraping.parse_import_export_table(
                    html_content=f.read(), metadata={"product": "Vinhos de mesa"}
                )
                == expected
            )
