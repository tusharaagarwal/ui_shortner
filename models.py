from datetime import datetime
from uuid import UUID

from typing import Type, Literal
from pydantic import BaseModel

from config import DEFAULT_DOMAIN

ACCOUNT_TYPE = ["free","paid"]


class ItemBase(BaseModel):
    created_at: datetime = datetime.now
    updated_at: datetime = datetime.now

class Account(ItemBase):
    account_type:Literal["free","paid"]

class Alias(ItemBase):
    name: str

class ShortUrl(ItemBase):
    id: UUID
    original_url: str
    domain:str = DEFAULT_DOMAIN
    alias: Type[Alias]