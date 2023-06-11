# Cafe Application
The project provides an API interface for the client cafe application, in particular the creation, 
editing and deletion of menus, creation and editing a shopping cart, and forming an order

## Software versions

python:3.11.3
PIP_VERSION:23.1.2
POETRY_VERSION:1.5.0

## Getting started

To get started with this project, follow the steps below:
1. Install [Docker](https://docs.docker.com/engine/install/) and [Docker Compose](https://docs.docker.com/compose/install/) on your computer if they are not already installed.
2. Clone the repository to your local machine.
3. Navigate to the root directory of the project.
4. configure `.env` file by assigning values to the variables defined in `.env.sample`
5. In the project directory, run `docker-compose up --build` to start the services.

After completing these steps, the project will be running and available at `http://localhost:8000/`.

## Creating superuser

To create a superuser, execute the following command:

`docker-compose exec webapp python project/manage.py createsuperuser`

Follow the on-screen instructions to set credentials for the superuser.

Open your web browser and go to `http://localhost:8000/admin/`. Log in with the superuser credentials you just created.


## Usage
To get the entire API schema of this application, you can open in browser endpoint `api/docs/`


## Database administration

To administer the database, you can use pgAdmin, which runs in a separate container. To access pgAdmin, follow these steps:

1. Open a browser and go to `http://localhost:5050/`.
2. Enter the login and password from your `.env` file to log in to pgAdmin.
3. Create a new connection to the necessary database
4. Connect to the database and perform the necessary operations.
