
<p align="center">
	<img width="200px" src="https://github.com/ar-russ/ufo-delivery/blob/main/docs/logo.png?raw=true" alt="logo"/>
</p>

# 🍟 UFO Delivery

A FastAPI-based project to explore and implement the Three-Tier-Architecture.

[![Pylint](https://github.com/ar-russ/ufo-delivery/actions/workflows/pylint.yml/badge.svg)](https://github.com/ar-russ/ufo-delivery/actions/workflows/pylint.yml)

## About this project

UFO Delivery is a backend project simulating a simple operator-assisted food delivery service. The concept is that user 
selects items from the menu, specifies their address and places an order, after which an operator collects it and 
dispathes the delivery to the user.

## Tech Stack

- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Alembic](https://alembic.sqlalchemy.org/en/latest/)
- [MySQL](https://www.mysql.com/)
- [Docker](https://www.docker.com/)
- [uv](https://github.com/astral-sh/uv)

## Documentation

The API documentation of this project is presented [here](docs/endpoints.md).

## Setup & Installation
- Make `.env` file using [.env.example](docs/.env.example) as template


- Clone the repository and run the following command to build the project:  
`docker-compose up --build`

- Apply database migrations:  
`alembic upgrade head`
