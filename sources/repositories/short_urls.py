from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from sources.domains.short_urls import ShortUrlDomain
from sources.models.short_urls import ShortUrlModel


class ShortUrlRepository:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def get(self, **kwargs) -> ShortUrlDomain:
        statement = select(ShortUrlModel).filter_by(**kwargs)
        execute = await self.session.execute(statement=statement)
        model = execute.scalar_one()
        domain = await self._to_domain(model=model)
        return domain

    async def all(self) -> list[ShortUrlDomain]:
        statement = select(ShortUrlModel)
        execute = await self.session.execute(statement=statement)
        models = execute.scalars()
        domains = [await self._to_domain(model=model) for model in models]
        return domains

    async def save(self, domain: ShortUrlDomain) -> ShortUrlDomain:
        model = await self._from_domain(domain=domain)
        self.session.add(instance=model)
        await self.session.commit()
        domain.id = model.id
        return domain

    async def _to_domain(self, model: ShortUrlModel) -> ShortUrlDomain:
        return ShortUrlDomain(
            id=model.id,
            slug=model.slug,
            source_url=model.source_url,
        )

    async def _from_domain(self, domain: ShortUrlDomain) -> ShortUrlModel:
        return ShortUrlModel(
            id=domain.id,
            slug=domain.slug,
            source_url=domain.source_url,
        )
