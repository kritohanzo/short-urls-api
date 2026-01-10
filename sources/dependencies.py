from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from sources.databases import get_session

Session = Annotated[AsyncSession, Depends(dependency=get_session)]
