import uvicorn
from fastapi import FastAPI
from fastapi.responses import JSONResponse

from src.contexts import DatabaseContext
from src.notification import services
from src.notification.settings import DOMAIN_NAME, ApiServerSettings, ApiSettings

api = FastAPI(debug=ApiSettings.DEBUG, docs_url=ApiSettings.DOCS_URL)
database_context = DatabaseContext(DOMAIN_NAME)


@api.get("/verify-user/{hexcode}")
def verify_user_view(hexcode: str):
    services.verify_user(
        database_context.unit_of_work,
        hexcode,
    )
    return JSONResponse(content={"message": "OK"}, status_code=200)


@api.get("/health-check")
def health_check():
    return JSONResponse(content={"message": "System up and running"}, status_code=200)


server_config = uvicorn.Config(
    api,
    host=ApiServerSettings.HOST,
    port=ApiServerSettings.PORT,
    reload=ApiServerSettings.RELOAD,
    workers=ApiServerSettings.WORKERS,
)
server = uvicorn.Server(server_config)
