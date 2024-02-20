from fastapi import HTTPException
import aiohttp

from src.api.v1.form.schemas import FormRequestSchema
from src.config import settings


class FormService:
    async def submit(self, form: FormRequestSchema):
        TELEGRAM_URL = f"https://api.telegram.org/bot{settings.TELEGRAM_TOKEN}/sendMessage"
        async with aiohttp.ClientSession() as session:
            data = {
                "chat_id": settings.TELEGRAM_CHAT_ID,
                "text": f"Name: {form.name}\nPhone: {form.phone}\nEmail: {form.email}\nMessage: {form.message}",
            }
            async with session.post(TELEGRAM_URL, data=data) as resp:
                response = await resp.json()
            if not response["ok"] or response["ok"] is not True:
                raise HTTPException(status_code=400, detail="Sending form failed")