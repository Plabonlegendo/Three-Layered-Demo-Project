# Three-Layered-Demo-Project

## Overview
This repository demonstrates a three-layered architecture design pattern, which divides the project into the following layers:

1. **Controller Layer**: Responsible for handling incoming requests and returning responses. It acts as the interface between the client and the business logic.
2. **Service Layer**: Contains the business logic and orchestrates the workflow between the controller and repository layers.
3. **Repository Layer**: Responsible for interacting with the data layer, such as databases or external data sources.

This structure ensures separation of concerns, improves maintainability, and promotes scalability of the application.

---

## Project Structure
```
Three-Layered-Demo-Project/
│
├── controller/        # Handles incoming requests and responses
│   └── controller.py
│
├── service/           # Contains business logic
│   └── service.py
│
├── repository/        # Interacts with data sources
│   └── repository.py
│
├── main.py            # Entry point of the application
├── pyproject.toml     # Poetry configuration file
└── README.md          # Project documentation
```

---

## Prerequisites

Ensure you have [Poetry](https://python-poetry.org/) installed. You can install it using pip:
```bash
pip install poetry
```

---

## Installation

1. Clone the repository:
```bash
git clone git@github.com:Plabonlegendo/Three-Layered-Demo-Project.git
cd Three-Layered-Demo-Project
```

2. Install dependencies using Poetry:
```bash
poetry install
```

---

## Running the Project

To start the application, run the `main.py` file:
```bash
python main.py
```

---

## How It Works

1. **Request Flow**: Incoming requests are routed to the controller layer.
2. **Business Logic**: The controller invokes the service layer to process the request.
3. **Data Access**: The service layer interacts with the repository layer to fetch or persist data.
4. **Response Flow**: The processed data is returned to the controller and sent back to the client.
