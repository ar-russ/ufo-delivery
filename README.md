# 🍟 UFO Delivery

A FastAPI-based project to explore and implement the Three-Tier-Architecture.

[![Pylint](https://github.com/ar-russ/ufo-delivery/actions/workflows/pylint.yml/badge.svg)](https://github.com/ar-russ/ufo-delivery/actions/workflows/pylint.yml)

## About this project

UFO Delivery is a backend project simulating a simple operator-assisted food delivery service. The concept is that user 
selects items from the menu, specifies their address and places an order, after which an operator collects it and 
dispathes the delivery to the user.

## Tech Stack

- FastAPI
- SQLAlchemy + Alembic
- MySQL
- Docker

## Documentation

The API documentation of this project is presented [here](docs/endpoints.md).

## Setup & Installation
- Make `.env` file using [.env.example](docs/.env.example) as template


- Clone the repository and run the following command to build the project:  
`docker-compose up --build`

- Apply database migrations:  
`alembic upgrade head`
