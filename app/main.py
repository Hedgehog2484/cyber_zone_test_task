import asyncio
import uvicorn

from fastapi import FastAPI

from api import setup_handlers
from load_config import config
from services.db import ConnectionsFactory, DAO


async def setup(app: FastAPI):
    db = DAO(await ConnectionsFactory(config.database_url.get_secret_value()).create())
    await db.create_tables()
    app.dependency_overrides[DAO] = db
    setup_handlers(app)


def main():
    app = FastAPI()
    asyncio.run(setup(app))
    uvicorn.run(app, host="0.0.0.0", port=8080)
