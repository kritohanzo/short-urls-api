import uvicorn
from fastapi import FastAPI

from sources.routers import routers
from sources.settings import settings

app = FastAPI()


for router in routers:
    app.include_router(router=router)


if __name__ == '__main__':
    uvicorn.run(
        app='sources.app:app',
        host=settings.SERVER_HOST,
        port=settings.SERVER_PORT,
    )
