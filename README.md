# Embrapa API

This application provides a RESTful API for accessing and searching data from the [Embrapa Vitibrasil website](http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_01), which is managed by Embrapa – The Brazilian Agricultural Research Corporation. The API enables users to retrieve, process, and analyze viticulture-related datasets, such as commercialization, exportation, and grape juice production, in a structured and programmatic way.

---

## Project Structure
```plaintext
Embrapa-API/
├── app/
│   ├── main.py      # Entry point of the application
│   ├── routers.py   # API endpoints definition
│   ├── scraping.py  # Web scraping utilities
│   ├── parser_csv.py # CSV parsing and processing
│   ├── services.py  # Business logic and data services
│   ├── auth.py        # Authentication and security logic
│   ├── models.py      # Data models
├── files/          # Data storage (CSV files)
├── tests/          # Automated tests
├── requirements.txt # Dependency management
└── README.md       # Project documentation
```

## Overview
This project is designed to provide a comprehensive API for accessing viticulture data from Embrapa. It includes functionalities for scraping data from the Embrapa Vitibrasil website, parsing CSV files, and serving this data through a RESTful API.

## Dependencies

- Python 3.11

---

## Getting Started


1. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

2. **Run the application:**
   ```sh
   uvicorn app.main:app --reload
   ```
3. **Access the API:**
   Open your browser and navigate to [http://localhost:8000/docs](http://localhost:8000/docs) to view the interactive API documentation provided by FastAPI.

## Contributing
Contributions are welcome! If you find a bug or have a feature request, please open an issue or submit a pull request. Make sure to follow the project's coding standards and include tests for new features.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
