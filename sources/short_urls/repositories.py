from collections.abc import Sequence
from typing import Any

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from sources.short_urls.models import ShortUrlModel


# TODO: базовый репозиторий нужон, а ещё DJANGO QUERYSET LIKE REPOSITORY!
class ShortUrlRepository:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def all(self) -> Sequence[ShortUrlModel]:
        statement = select(ShortUrlModel)
        result = await self.session.execute(statement=statement)
        return result.scalars().all()

    async def get(self, **kwargs: Any) -> ShortUrlModel:
        statement = select(ShortUrlModel).filter_by(**kwargs)
        result = await self.session.execute(statement=statement)
        return result.scalar_one()

    async def create(self, **kwargs: Any) -> ShortUrlModel:
        short_url = ShortUrlModel(**kwargs)
        self.session.add(instance=short_url)
        await self.session.commit()
        return short_url

    async def save(self, instance: ShortUrlModel) -> None:
        await self.session.merge(instance=instance)
        await self.session.commit()
