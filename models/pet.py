from models.category import Category
from models.tag import Tag
from typing import List


class Pet:
    id: int
    category: Category
    name: str
    photoUrls: List[str]
    tags: List[Tag]
    status: str



