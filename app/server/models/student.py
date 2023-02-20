from typing import Optional

from pydantic import BaseModel, EmailStr, Field


class StudentSchema(BaseModel):
    fullname: str = Field(...)
    email: EmailStr = Field(...)
    course_of_study: str = Field(...)
    year: int = Field(..., gt=0, lt=9)

    class Config:
        schema_extra = {
            "example":     {
                "fullname": "Guillaume DUPUY",
                "email": "guillaume.dupuy@ynov.com",
                "course_of_study": "Master AI & Big Data",
                "year": 4
            }
        }


class UpdateStudentModel(BaseModel):
    fullname: Optional[str]
    email: Optional[EmailStr]
    course_of_study: Optional[str]
    year: Optional[int]

    class Config:
        schema_extra = {
            "example":     {
                "fullname": "Guillaume DUPUY",
                "email": "guillaume.dupuy@ynov.com",
                "course_of_study": "Master AI & Big Data",
                "year": 4
            }
        }

def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
