from random import choice
from string import ascii_letters, digits
from typing import Final

from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession

from sources.short_urls.domains import ShortUrlDomain
from sources.short_urls.exceptions import GenerateSlugException
from sources.short_urls.repositories import ShortUrlRepository


class ShortUrlService:
    SLUG_CHARS: Final[str] = ascii_letters + digits
    SLUG_LENGHT: Final[int] = 6
    SLUG_GENERATION_ATTEMPS: Final[int] = 5

    def __init__(self, session: AsyncSession):
        self.repository = ShortUrlRepository(session=session)

    async def all(self) -> list[ShortUrlDomain]:
        domains = await self.repository.all()
        return domains

    async def get(self, slug: str, as_visitor: bool = False) -> ShortUrlDomain:
        domain = await self.repository.get(slug=slug)

        if as_visitor:
            domain.visitors += 1
            domain = await self.repository.save(domain=domain)

        return domain

    async def create(self, source_url: str) -> ShortUrlDomain:
        slug = await self._generate_slug()
        domain = await self.repository.create(domain=ShortUrlDomain(slug=slug, source_url=source_url))
        return domain

    async def _generate_slug(self) -> str:
        for _ in range(self.SLUG_GENERATION_ATTEMPS):
            slug = "".join([choice(self.SLUG_CHARS) for _ in range(self.SLUG_LENGHT)])

            try:
                await self.repository.get(slug=slug)
            except NoResultFound:
                return slug

        raise GenerateSlugException()
