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

    # def __init__(self) -> None:
    #     self.category = Category()
    #     self.tags = []

    # def AddTag(self, id: int, name: str):
    #     tag = Tag()
    #     tag.id = id
    #     tag.name = name
    #     self.tags.append(tag)


        # self.id = id
        # self.category = Category()
        # self.name = name
        # self.photo_urls = photo_urls
        # self.tags = tags
        # self.status = status

    # def __init__(self, id: int, name: str) -> None:
    #     self.id = id
    #     self.name = name

