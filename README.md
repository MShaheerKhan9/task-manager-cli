\# Task Manager (CLI + FastAPI)



A simple yet well-structured task manager application built with Python, following clean separation of concerns.

The project supports both a Command Line Interface (CLI) and a REST API using FastAPI, with persistent file-based storage.



This project is designed as a learning-focused backend foundation, following patterns used in real-world backend applications.



---



\## Features



\### Core Functionality

\- Add tasks

\- Remove tasks

\- Mark tasks as completed

\- View daily task progress

\- Retrieve individual tasks

\- Automatic daily task reset with history logging



\### Interfaces

\- ✅ Command Line Interface (CLI)

\- ✅ REST API (FastAPI)



\### Persistence

\- File-based task storage (`tasks.txt`)

\- Daily history logs (`log.txt`, `last\_log.txt`)



---



\## Tech Stack

\- Python 3

\- FastAPI

\- Pydantic

\- Uvicorn

\- Pytest (for testing)



---



\## Project Structure



.

├── api.py # FastAPI routes (HTTP layer only)

├── cli.py # Command-line interface

├── core.py # Core business logic (TaskManager)

├── storage.py # File persistence logic

├── services/

│ └── task\_services.py # Service layer shared by CLI \& API

├── tests/

│ └── test\_core.py # Unit tests for core logic

├── requirements.txt # Project dependencies

├── README.md





---



\## Architecture Overview



\### `core.py`

Contains all domain rules and business logic.

This is the \*\*single source of truth\*\* and is fully unit-tested.



\### `services/`

Acts as a service layer that adapts core logic for different interfaces (CLI \& API).

No direct file or HTTP handling here.



\### `api.py`

Pure HTTP layer:

\- Request parsing

\- Response formatting

\- Error translation to HTTP status codes



\### `cli.py`

CLI adapter using the same service layer as the API.



---



\## Running the Project



\### 1. Create Virtual Environment

python -m venv .venv

source .venv/bin/activate # Linux / Mac

.venv\\Scripts\\activate # Windows





\### 2. Install Dependencies

pip install -r requirements.txt





\### 3. Run FastAPI Server

uvicorn api:app --reload





Open in browser:

http://127.0.0.1:8000/docs





---



\## API Endpoints (Summary)



| Method | Endpoint             | Description                  |

|------|----------------------|------------------------------|

| GET  | /tasks               | List all tasks               |

| POST | /tasks               | Add a new task               |

| GET  | /tasks/{id}          | Get a single task            |

| DELETE | /tasks/{id}        | Delete a task                |

| PUT  | /tasks/{id}/done     | Mark task as completed       |

| GET  | /progress            | Daily task progress          |



---



\## Testing



\- Unit tests implemented using \*\*pytest\*\*

\- Core business logic is fully tested

\- Tests are isolated and do not affect real data files



Run tests:

pytest





---



\## Error Handling



Custom domain exceptions:

\- `TaskNotFoundError`

\- `TaskAlreadyExists`

\- `TaskDoneAlreadyError`



Errors are safely converted to proper HTTP responses in the API layer.



---



\## Git \& Persistence Notes



\- Runtime data files are ignored by Git:

&nbsp; - `tasks.txt`

&nbsp; - `log.txt`

&nbsp; - `last\_log.txt`

\- Only source code, configuration, and tests are version-controlled



---



\## Future Improvements

\- API endpoint tests

\- Improved API validation

\- Authentication

\- Replace file storage with a database

\- Dockerization



---



\## Learning Goals of This Project

\- Clean separation of concerns

\- Service-layer architecture

\- Unit testing with pytest

\- API design with FastAPI

\- Writing production-ready backend code

