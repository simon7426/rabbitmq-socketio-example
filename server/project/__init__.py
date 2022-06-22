import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from project.apis import alive, publish
from project.utils import declare_queue


log = logging.getLogger("uvicorn")

def create_app() -> FastAPI:
    app = FastAPI()
    app.add_middleware(
        CORSMiddleware,
        allow_origins=['*']
    )

    # * Adding Routers to app *#
    app.include_router(alive.router)
    app.include_router(publish.router)

    return app


app = create_app()

@app.on_event("startup")
async def startup_event():
    log.info("Starting up...")
    await declare_queue()


@app.on_event("shutdown")
async def shutdown_event():
    log.info("Shutting down...")
