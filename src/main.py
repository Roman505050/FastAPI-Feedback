from fastapi import FastAPI, Request
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from starlette.responses import JSONResponse
from starlette.staticfiles import StaticFiles
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY
from fastapi.templating import Jinja2Templates

from src.api.v1.form.router import router as form_router

app = FastAPI()
templates = Jinja2Templates("web")

@app.get("/", include_in_schema=False)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.exception_handler(RequestValidationError)
async def request_validation_exception_handler(
    request: Request, exc: RequestValidationError
) -> JSONResponse:
    return JSONResponse(
        status_code=HTTP_422_UNPROCESSABLE_ENTITY,
        content={"detail": jsonable_encoder(exc.errors(), exclude={"url", "input"})})


app.include_router(form_router, prefix="/api/v1/form", tags=["form"])
