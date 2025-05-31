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

1. **Install Python 3.11:**Add commentMore actions
   If you don't have Python 3.11 installed, download it from the [official Python website](https://www.python.org/downloads/) or use a package manager:

   - **Homebrew (macOS):**
     ```sh
     brew install python@3.11
     ```
   - **Windows:**
     Download and run the installer from [python.org](https://www.python.org/downloads/).

   - **Linux (Ubuntu):**
     ```sh
     sudo apt-get update
     sudo apt-get install python3.11 python3.11-venv python3.11-dev
     ```

2. **Create and activate a virtual environment:**
   It's recommended to use a virtual environment to manage dependencies.

   ```sh
   python3.11 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```sh
   uvicorn app.main:app --reload
   ```
5. **Access the API:**
   Open your browser and navigate to [http://localhost:8000/docs](http://localhost:8000/docs) to view the interactive API documentation provided by FastAPI.

---

## Running with Docker

You can run the application easily using Docker:

1. **Start the application:**
   ```sh
   docker compose up --build -d
   ```
2. **Access the API:**
   Open [http://localhost:8000/docs](http://localhost:8000/docs) in your browser.

---

## Running Tests

Automated tests are located in the `tests/` directory. To run the tests, use:

```sh
pytest
```

---
