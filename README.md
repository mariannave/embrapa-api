# Embrapa API

This application provides a RESTful API for accessing and searching data from the Embrapa Vitibrasil website ([http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_01](http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_01)), which is managed by Embrapa – The Brazilian Agricultural Research Corporation. The API enables users to retrieve, process, and analyze viticulture-related datasets, such as commercialization, exportation, and grape juice production, in a structured and programmatic way.

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
├── files/          # Data storage (CSV files)
├── tests/          # Automated tests
├── requirements.txt # Dependency management
└── README.md       # Project documentation
```

## Overview
This project is designed to provide a comprehensive API for accessing viticulture data from Embrapa. It includes functionalities for scraping data from the Embrapa Vitibrasil website, parsing CSV files, and serving this data through a RESTful API. The application is built using FastAPI, which allows for high performance and easy integration with modern web technologies.

## Features
- **Data Scraping:** Automatically fetches and parses data from the Embrapa Vitibrasil website.
- **CSV Processing:** Reads and processes CSV files containing viticulture data.
- **RESTful API:** Provides endpoints for accessing viticulture data, including commercialization, exportation, and grape juice production.
- **Interactive Documentation:** Automatically generated API documentation using FastAPI's OpenAPI support.
- **Testing Suite:** Includes unit and integration tests to ensure the reliability of the application.
- **Dependency Management:** Uses `requirements.txt` for managing Python package dependencies.
- **Modular Design:** Organized into components for easy maintenance and scalability.
- **Logging:** Configured logging for debugging and monitoring purposes.

## Components Overview
This project is structured into several components, each serving a specific purpose in the overall functionality of the API. Below is a brief overview of each component:

### Components

#### 1. `app/main.py`
- **Purpose:** Entry point of the application.
- **Details:** Initializes the FastAPI app, sets up logging, and includes the API routers. Configures OpenAPI documentation and provides a description of the API.

#### 2. `app/routers.py`
- **Purpose:** Defines the API endpoints.
- **Details:** Organizes and registers the various routes/endpoints for accessing different datasets and functionalities. Handles HTTP requests and responses.

#### 3. `app/scraping.py`
- **Purpose:** Web scraping utilities.
- **Details:** Contains functions and classes for fetching and parsing data from the Embrapa Vitibrasil website. Responsible for extracting raw data to be processed or stored.

#### 4. `app/parser_csv.py`
- **Purpose:** CSV parsing and processing.
- **Details:** Provides utilities for reading, validating, and transforming CSV files. Ensures data consistency and prepares it for API responses.

#### 5. `app/services.py`
- **Purpose:** Business logic and data services.
- **Details:** Implements core logic for data manipulation, aggregation, and transformation. Acts as an intermediary between the routers and data sources (scraping or CSV).

#### 6. `files/`
- **Purpose:** Data storage.
- **Details:** Contains CSV files with viticulture data, such as commercialization, exportation, and grape juice production. These files are used as data sources for the API.

#### 7. `tests/`
- **Purpose:** Automated tests.
- **Details:** Contains unit and integration tests to ensure the correctness and reliability of the application components.

#### 8. `requirements.txt`
- **Purpose:** Dependency management.
- **Details:** Lists all Python packages required to run the application, including FastAPI, BeautifulSoup, and others.

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
4. **Explore the API:**
   Use the interactive documentation to test the endpoints and understand the available functionalities.


## Contributing
Contributions are welcome! If you find a bug or have a feature request, please open an issue or submit a pull request. Make sure to follow the project's coding standards and include tests for new features.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
