from fastapi import FastAPI

from sources.apis.routers import routers

app = FastAPI()

for router in routers:
    app.include_router(router=router)
