from dataclasses import dataclass


@dataclass
class PostRecord:
    user_id: int
    id: int
    title: str
    body: str