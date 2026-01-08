from random import choice
from string import ascii_letters, digits
from typing import Final

from sqlalchemy.ext.asyncio import AsyncSession

from sources.domains.short_urls import ShortUrlDomain
from sources.repositories.short_urls import ShortUrlRepository


class ShortUrlService:
    SLUG_CHARS: Final[str] = ascii_letters + digits
    SLUG_LENGHT: Final[int] = 6

    def __init__(self, session: AsyncSession):
        self.repository = ShortUrlRepository(session=session)

    async def get(self, slug: str) -> ShortUrlDomain:
        domain = await self.repository.get(slug=slug)
        return domain

    async def all(self) -> list[ShortUrlDomain]:
        domains = await self.repository.all()
        return domains

    async def create(self, source_url: str) -> ShortUrlDomain:
        slug = await self._generate_slug()
        domain = ShortUrlDomain(slug=slug, source_url=source_url)
        await self.repository.save(domain=domain)
        return domain

    async def _generate_slug(self) -> str:
        return "".join([choice(self.SLUG_CHARS) for _ in range(self.SLUG_LENGHT)])
