from pydantic import BaseModel , Field, field_validator, model_validator, computed_field, ConfigDict, EmailStr, AnyUrl
# BaseModel: for checking if the incoming data is valid or not
# Field: Required field, without this the code will throw error

from typing import Optional, Literal # optional to give value in the field 

# Pydantic Model: any class with inheriting BaseModel
class Category(BaseModel):
    name : Literal['Starter','Main Course','Desert','Beverage'] # User must enter category value from these only


class Model(BaseModel):
    # Model configuration using Pydantic's ConfigDict
    model_config = ConfigDict(
    extra='allow',          # Controls handling of extra/unexpected fields:
                            # 'allow' → keep them,
                            # 'forbid' → raise error,
                            # 'ignore' → drop silently.
    frozen=True,            # Makes the model immutable (read‑only).
                            # Once created, you cannot change field values.
    strict=True,            # Enforces strict type checking.
                            # Example: passing "123" as a string to an int field will raise an error.
    validate_assignment=True # Validates data types when editing attributes.
                            # Prevents invalid updates after initialization.
)
    # field     :  value
    id          :  int = Field(...)
    name        :  str
    price       :  float = Field(...,gt=0,description="Item Price") # added constraints and description for the field
    category    :  Category
    is_available : bool = Field(default=True)
    description :  Optional[str] = None
    # email : EmailStr -> checks if valid valid email is given
    # url : AnyUrl -> checks if valid url is given

    # All Validators must be declared inside Model Class
    # field Validator (only works on single field)
    @field_validator('name',mode='after')
    @classmethod
    def title_name(cls,value): #value = "Paneer TIkKA --> Paneer Tikka"
        return value.title()

    # Model Validator (works on multiple fileds)
    @model_validator(mode='after')
    def check_available(self):
        if self.is_available and self.price <= 0:
            raise('Available item must be greater than 0')
        return self

    # Computed Field (adds new field with the help of already existing field)
    @computed_field
    @property
    def price_tax(self) -> float:
        return round(self.price * 1.05, 2)

item = Model(id=1, name='Paneer TIkKA', price=100, category=Category(name='Starter'), is_available=True)

# the 'item' is an object of a Model class & objects cant be passed to other functions

#1. model_dump() is used to convert 'item' object to dictionary
# will only work inside python (in serialization)
print('Dictionary model_dump()')
print(item.model_dump())

#2. model_dump_json() -> object over the internet or the website, Out of Python (out serialization)
print('JSON model_dump_json()')
print(item.model_dump_json())