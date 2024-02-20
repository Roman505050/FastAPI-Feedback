from pydantic import BaseModel, Field, EmailStr

class FormRequestSchema(BaseModel):
    name: str = Field(..., min_length=2, max_length=50, title="Name", description="Name of the form")
    phone: str = Field(..., min_length=12, max_length=13, title="Phone", description="Phone number of the form")
    email: EmailStr = Field(..., min_length=3, max_length=50, title="Email", description="Email of the form")
    message: str = Field(..., min_length=10, max_length=750, title="Message", description="Message of the form")