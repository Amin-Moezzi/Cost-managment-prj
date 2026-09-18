from pydantic import BaseModel, Field, field_validator
import re

description_regex = r"^[A-Za-z][A-Za-z0-9 ]*$"

class BaseCostSchema(BaseModel):
    description : str = Field(..., description= "Enter description of Cost")
    amount : float = Field(..., ge= 0)

    @field_validator("description")
    def description_field(cls, value):
        if not re.fullmatch(description_regex, value):
            raise ValueError (f"{value} is not a vaild name")
        return value
    
class CostCreateSchema(BaseCostSchema):
    pass

class CostResponseSchema(BaseCostSchema):
    id : int = Field(..., description= " unique cost id")

class CostUpdateSchema(BaseCostSchema):
    pass

