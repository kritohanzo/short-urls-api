from pydantic import BaseModel


class CreateShortUrlRequestSchema(BaseModel):
    source_url: str


class ShortUrlSchema(BaseModel):
    source_url: str
    short_url: str
    visitors: int
