from decimal import Decimal
from enum import Enum
from pydantic import BaseModel, Field, UUID4


class DifficultyEnum(str, Enum):
    BEGINNER = "beginner"
    INTERMEDIATE = "intermediate"
    ADVANCED = "advanced"


class CourseModel(BaseModel):
    courseid: UUID4

    title: str = Field(min_length=1, max_length=55)
    subtitle: str = Field(min_length=1, max_length=150)
    description: str = Field(min_length=1, max_length=450)

    instructorid: UUID4

    price: Decimal = Field(max_digits=8, decimal_places=2)
    discount_price: Decimal = Field(max_digits=8, decimal_places=2)

    thumbnail: str
    promovideo: str

    difficalulty_level: DifficultyEnum

    total_duration_in_seconds: int
    ispublished: bool