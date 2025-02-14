from .base import NoSQLBaseDocument
from .types import DataCategory
from abc import ABC
from enum import StrEnum
from pydantic import UUID4, Field
from typing import Optional


class DataCategory(StrEnum):
    PROMPT = "prompt"
    QUERIES = "queries"
    INSTRUCT_DATASET_SAMPLES = "instruct_dataset_samples"
    INSTRUCT_DATASET = "instruct_dataset"
    PREFERENCE_DATASET_SAMPLES = "preference_dataset_samples"
    PREFERENCE_DATASET = "preference_dataset"
    POSTS = "posts"
    ARTICLES = "articles"
    REPOSITORIES = "repositories"

class Document(NoSQLBaseDocument, ABC):
    content: dict
    platform: str
    author_id: UUID4 = Field(alias="author_id")
    author_full_name: str = Field(alias="author_full_name")


class RepositoryDocument(Document):
    name: str
    link: str
    class Settings:
        name = DataCategory.REPOSITORIES


class PostDocument(Document):
    image: Optional[str] = None
    link: str | None = None
    class Settings:
        name = DataCategory.POSTS


class ArticleDocument(Document):
    link: str
    class Settings:
        name = DataCategory.ARTICLES

class UserDocument(NoSQLBaseDocument):
    first_name: str
    last_name: str
    class Settings:
        name = "users"
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"