# Django Interview Task

## Live demo

Live demo is available at [https://skrepka.demo.zayats.dev/](https://skrepka.demo.zayats.dev/)

Admin panel is available at [https://skrepka.demo.zayats.dev/admin/](https://skrepka.demo.zayats.dev/admin/)

Credentials:
- username: ```admin```
- password: ```admin```

## Installation

### Local

1. Clone the repository
    ```bash
    git clone git@github.com:MaksimZayats/django-interview-task.git
    ```
2. Create a virtual environment
    ```bash
    python -m venv .venv
    ```
3. Activate the virtual environment
    ```bash
    source .venv/bin/activate
    ```
4. Configure the environment variables (see `.env.example`)
    ```bash
    cp .env.example .env
    ```
5. Install the requirements
    ```bash
    pip install -r requirements.txt
    ```
6. Run the migrations
    ```bash
    make migrate
    ```
7. Run the server
    ```bash
    make run.server.local
    ```

### Docker

1. Clone the repository
    ```bash
    git clone git@github.com:MaksimZayats/django-interview-task.git
    ```
2. Configure the environment variables (see `.env.example`)
    ```bash
    cp .env.example .env
    ```
3. Run the docker compose
    ```bash
    docker compose up -d
    ```


## Usage

### Swagger documentation

Swagger documentation is available at `/docs/` endpoint.

### Admin panel

Admin panel is available at `/admin/` endpoint.

Default credentials:
- username: ```admin```
- password: ```admin```

### Solution to given task

The solution to the given task is available at `/contracts/{id}/get_manufacturer_ids/` endpoint. Check the Swagger documentation for more details.

## Room for improvements

- Add authentication, authorization, permissions
- Add tests
- etc.
