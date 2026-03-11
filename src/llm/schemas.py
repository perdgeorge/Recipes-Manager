from src.api.schemas import BaseSchema
from pydantic import Field
from src.llm.enums import Role


class IngredientPrompt(BaseSchema):
    name: str = Field(..., examples=["Broccoli"])
    quantity: str = Field(..., examples=["100 grams"])
    is_vegan: bool = Field(..., examples=[True])
    calories: int = Field(..., examples=[34])


class ChatMessage(BaseSchema):
    role: Role = Field(..., examples=["user", "system", "assistant"])
    content: str = Field(examples=["Recipe"])


class ChatResponse(BaseSchema):
    ingredients: list[IngredientPrompt] = Field(
        default_factory=list,
        examples=[
            {
                "name": "Broccoli",
                "quantity": "100 grams",
                "is_vegan": True,
                "calories": 34,
            }
        ],
    )
    total_calories: int = Field(examples=[34])
