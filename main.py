# pylint: disable=missing-function-docstring
from fastapi import FastAPI
from uvicorn import Server, Config

from src.routes import items, users, orders
from config.config import settings


def build_app() -> FastAPI:
    app = FastAPI()

    app.include_router(items.router)
    app.include_router(users.router)
    app.include_router(orders.router)

    return app


def main() -> None:
    config = Config(
        app=build_app(),
        host=settings.host,
        port=settings.port,
    )

    server = Server(config)
    server.run()


if __name__ == '__main__':
    main()
