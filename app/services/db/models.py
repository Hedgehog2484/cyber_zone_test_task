from dataclasses import dataclass


@dataclass
class User:
    id: int
    username: str
    password_hash: str
    created_at: float
    updated_at: float


@dataclass
class Booking:
    id: int
    user_id: int
    start_time: float
    end_time: float
    comment: str
