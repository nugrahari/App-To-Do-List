# Django & Vite.js Project with Docker Compose

This project contains a Django backend and a Vite.js frontend, both of which can be run using Docker Compose.

## Prerequisites

Ensure you have the following installed on your machine:

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Project Setup

This repository is structured with a Django application for the backend and a Vite.js application for the frontend.

### Folder Structure


### 1. Clone the repository

First, clone this repository to your local machine.

```bash
git clone https://github.com/...
cd yourproject
```

### 2. Build Docker Containers
To build the containers for both Django and Vite.js, run the following command:
```bash
docker-compose up --build
```
This will:

- Build the Django application inside the django service.
- Build the Vue.js frontend inside the vue service.

### 3. Accessing the Application
Once the containers are up and running, you can access the applications via the following URLs:

- Django (Backend): http://localhost:8000 
(default superadmin: username:admin, password:admin)
- Vite.js (Frontend): http://localhost:5173

### 4. Running Django Migrations
To set up the database for Django, you need to run the migrations inside the web container:

```bash
docker-compose exec web python manage.py migrate
```
If you need to create a superuser for the Django admin, you can run:
```
docker-compose exec web python manage.py createsuperuser
```

### 5. Stopping the Application
To stop the running containers, press Ctrl + C in the terminal where Docker Compose is running, or run:
```bash
docker-compose down
```
### 6. Rebuilding the Containers
If you make changes to the Dockerfile or docker-compose.yml and need to rebuild the containers, use:
```
docker-compose up --build
```

