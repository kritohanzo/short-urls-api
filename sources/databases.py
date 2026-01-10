from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker


from sources.settings import settings

engine = create_async_engine(url=settings.postgres_url)


sessionmaker = async_sessionmaker(bind=engine, expire_on_commit=False)


async def get_session():
    async with sessionmaker() as session:
        yield session
