from pydantic import BaseModel, ConfigDict


class AddShortUrlSchema(BaseModel):
    source_url: str


class ShortUrlSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    slug: str
    source_url: str
    visitors: int
