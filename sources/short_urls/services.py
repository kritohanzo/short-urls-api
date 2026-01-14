from collections.abc import Sequence
from random import choice
from string import ascii_letters, digits
from typing import Final

from sqlalchemy.exc import NoResultFound

from sources.short_urls.exceptions import GenerateSlugException
from sources.short_urls.models import ShortUrlModel
from sources.short_urls.repositories import ShortUrlRepository


class SlugGenerator:
    SLUG_CHARS: Final[str] = ascii_letters + digits
    SLUG_LENGHT: Final[int] = 6
    SLUG_GENERATION_ATTEMPS: Final[int] = 5

    def __init__(self, repository: ShortUrlRepository) -> None:
        self.repository = repository

    async def generate(self) -> str:
        for _ in range(self.SLUG_GENERATION_ATTEMPS):
            slug = ''.join([choice(self.SLUG_CHARS) for _ in range(self.SLUG_LENGHT)])

            try:
                await self.repository.get(slug=slug)
            except NoResultFound:
                return slug

        raise GenerateSlugException()


class ShortUrlService:
    def __init__(self, repository: ShortUrlRepository) -> None:
        self.repository = repository

    async def all(self) -> Sequence[ShortUrlModel]:
        return await self.repository.all()

    async def get(self, slug: str) -> ShortUrlModel:
        return await self.repository.get(slug=slug)

    async def visit(self, short_url: ShortUrlModel) -> None:
        short_url.visitors += 1
        await self.repository.save(instance=short_url)

    async def create(self, source_url: str) -> ShortUrlModel:
        generator = SlugGenerator(repository=self.repository)
        slug = await generator.generate()
        return await self.repository.create(slug=slug, source_url=source_url)
