from sqlalchemy.ext.asyncio import create_async_engine

from sources.settings import settings

engine = create_async_engine(url=settings.postgres_url)
