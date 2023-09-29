import asyncpg
import datetime

from typing import List, Optional

from services.db.models import User, Booking


class ConnectionsFactory:
    def __init__(self, database_url: str):
        self.db_url = database_url

    async def create(self) -> asyncpg.Connection:
        """ Creates new asyncpg.Connection and returns it. """
        conn = await asyncpg.connect(self.db_url)
        return conn


class DAO:
    """ Class with the methods to interactions with the db. """
    def __init__(self, connection: asyncpg.Connection):
        self._conn = connection

    async def create_tables(self) -> None:
        """ Creates all tables if don't exists. """
        await self._conn.execute("""CREATE TABLE IF NOT EXISTS users(
            id SERIAL PRIMARY KEY,
            username VARCHAR,
            password VARCHAR,
            created_at TIMESTAMP,
            updated_at TIMESTAMP
        )""")

        await self._conn.execute("""CREATE TABLE IF NOT EXISTS bookings(
        id SERIAL PRIMARY KEY,
        user_id INTEGER REFERENCES users(id),
        start_time TIMESTAMP,
        end_time TIMESTAMP,
        comment VARCHAR
        )""")

    async def add_user(self, username: str, password_hash: str) -> User:
        current_timestamp = datetime.datetime.now().timestamp()
        await self._conn.execute("INSERT INTO users(username, password, created_at, updated_at) VALUES ($1, $2, $3, $4)",
                                 username, password_hash, current_timestamp, current_timestamp)
        resp = await self._conn.fetchrow("SELECT * FROM users WHERE username=$1", username)
        return User(
            id=resp["id"],
            username=resp["username"],
            password_hash=resp["password"],
            created_at=resp["created_at"],
            updated_at=resp["updated_at"]
        )

    async def get_user_by_id(self, user_id: int) -> None:
        resp = await self._conn.fetchrow("SELECT * FROM users WHERE id=$1", user_id)
        return User(
            id=resp["id"],
            username=resp["username"],
            password_hash=resp["password"],
            created_at=resp["created_at"],
            updated_at=resp["updated_at"]
        )

    async def get_user_by_username(self, username: str) -> None:
        pass

    async def delete_user_by_id(self, user_id: int) -> None:
        pass

    async def delete_user_by_username(self, username: str) -> None:
        pass

    async def add_booking(
            self,
            user_id: int,
            start_time: float,
            end_time: float,
            comment: str
    ) -> Optional[Booking]:
        pass

    async def get_all_bookings_by_user_id(self, user_id: int) -> Optional[List[Booking]]:
        pass

    async def delete_booking_by_id(self, booking_id: int) -> None:
        pass

    async def disconnect(self) -> None:
        """ Closes connection to the database. """
        await self._conn.close()
