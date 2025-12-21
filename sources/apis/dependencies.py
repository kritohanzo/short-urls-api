from sources.databases.sessions import get_session
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Annotated

Session = Annotated[AsyncSession, Depends(dependency=get_session)]
