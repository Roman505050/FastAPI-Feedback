from fastapi import APIRouter

from src.api.v1.form.schemas import FormRequestSchema
from src.services.form import FormService

router = APIRouter()

@router.post(
    path="/submit",
    responses={
        200: {
            "description": "Successful response",
            "content": {
                "application/json": {
                    "example": {"message": "ok"}
                }
            },
        },
        400: {
            "description": "Bad request",
            "content": {
                "application/json": {
                    "example": {"detail": "Sending form failed"}
                }
            },
        },
    },
)
async def submit(request_body: FormRequestSchema):
    await FormService().submit(form=request_body)
    return {"message": "ok"}