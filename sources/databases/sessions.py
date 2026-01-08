from sqlalchemy.ext.asyncio import async_sessionmaker

from sources.databases.engines import engine

sessionmaker = async_sessionmaker(bind=engine, expire_on_commit=False)


async def get_session():
    async with sessionmaker() as session:
        yield session
