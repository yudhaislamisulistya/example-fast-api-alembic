from typing import Union, List, Any
from fastapi import FastAPI, Path, Query, Body, Cookie, Header, Form, File, UploadFile, HTTPException
from pydantic import BaseModel, Field, HttpUrl, EmailStr
from enum import Enum
from typing_extensions import Annotated

# app = FastAPI()

# class Item(BaseModel):
#     name: str
#     price: float
#     is_offer: Union[bool, None] = None

# @app.get("/")
# def read_root():
#     return {"Hello": "World"}

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}

# @app.put("/items/{item_id}")
# def update_item(item_id: int, item: Item):
#     return {"item_name": item.name, "item_id": item_id}

app = FastAPI()
app_two = FastAPI()

@app.get("/")
async def root():
    return {"message": "Selamat Datang"}


# 2.1. Path Parameters
# @app.get("/items/{item_id}")
# async def read_item(item_id):
#     return {"item_id": item_id}

# 2.2. Path parameters with Types
# @app.get("/items/{item_id}")
# async def read_item(item_id: int):
#     return {"item_id": item_id}

# 2.3. Data Convertion is a default behavior in a FastAPI, each we define a funcion parameter with a type will be converted to that type automatically

# 2.4. Data Validation is a default behavior in a FastAPI, when we do a input string data, but we define a function parameter with a type integer, it will be error and response will see a nice pretty JSON error message

# 2.5. Documentation is a default feature by FastAPI, when we make a operation as get, it will be docs

# 2.6. Pydanctic Model, all the data validation is performed under the hood by Pydantic, it is a library that uses Python type annotations to validate the key-value pairs in a dictionary

# 2.7. Order matters

# @app.get("/users/me")
# async def read_user_me():
#     return {"user_id": "the current user"}


# @app.get("/users/{user_id}")
# async def read_user(user_id: int):
#     return {"user_id": user_id}

# 2.8. Predefined Values

# class ModelName(str, Enum):
#     alexnet = "alexnet"
#     resnet = "resnet"
#     lenet = "lenet"

# @app.get("/models/{model_name}")
# async def get_model(model_name: ModelName):
#     if model_name is ModelName.alexnet:
#         return {"moddel_name": model_name, "message": "Deep Learning FTW"}
    
#     if model_name.value == "lenet":
#         return {"model_name": model_name, "message": "LeCNN all the images"}
    
#     return {"model_name": model_name, "message": "Have some residuals"}

# 3. Query Paramaters is a parameter that goes after the ? in a URL, and separated by &
# 3.1. Query Paramater

# fake_items_db = [
#     {
#         "item_name": "Foo"
#     },
#     {
#         "item_name": "Bar"
#     },
#     {
#         "item_name": "Baz"
#     }
# ]

# @app.get("/items/")
# async def read_item(skip: int = 0, limit: int = 2):
#     return fake_items_db[skip: skip + limit]

# 3.2 Query Paramaters with Optional Parameters

# @app.get("/items/{item_id}")
# async def read_item(item_id: str, q: Union[str, None] = None):
#     if q:
#         return {"item_id": item_id, "q": q}
#     return {"item_id": item_id}

# 3.3 Query Paramater type Conversion
# @app.get("/items/{item_id}")
# async def read_item(item_id: str, q: Union[str, None] = None, short : bool = None):
#     item = {"item_id": item_id}
#     if q:
#         item.update({"q": q})
#     if not short:
#         item.update(
#             {"description": "This is an amazing item that has a long description"}
#         )
#     return item

# 3.4. Multiple Path and Query Parameters
# @app.get("/users/{user_id}/items/{item_id}")
# async def read_user_item(user_id: int, item_id: str, q: Union[str, None] = None, short: bool = False):
#     item = {"item_id": item_id, "owner_id": user_id}
#     if q:
#         item.update({"q": q})
#     if not short:
#         item.update({"description": "This is an amazing item that has a long description"})
    
#     return item

# 3.5 Required Query Paramaters

# @app.get("/items/{item_id}")
# async def read_item(item_id: str, needy: str):
#     return {"item_id": item_id, "needy": needy}

# 4. Request Body
# 4.1 Pydanctic BaseModel
# class Item(BaseModel):
#     name: str
#     description: Union[str, None] = None
#     price: float
#     tax: Union[float, None] = None
    
# @app.post("/items/")
# async def create_item(item: Item):
#     return item

# 4.2 Request Body + path + Query Paramater
# class Item(BaseModel):
#     name: str
#     description: Union[str, None] = None
#     price: float
#     tax: Union[str, None] = None
    
# @app.post("/items/{item_id}")
# async def create_item(item_id: int, item: Item, q: Union[str, None] = None):
#     result = {"item_id": item_id, **item.dict()}
#     if q: 
#         result.update({"q": q})
#     return result

# 5. Path Parameter and Numeric Validation
# 5.1 Still Path Paramater and Numeric Validation
# @app.get("/items/{item_id}")
# async def read_items(
#     item_id: Annotated[int, Path(title="The ID of the item to get", ge=0, le=1000)],
#     size: Annotated[float, Query(gt=0, lt=10.5)] = None
# ):
#     results = {"item_id": item_id, "size": size}
#     return results

# 6. Query Paramater and String Validations
# 6.1 Query Parameter dan String Validations

# @app.get("/items/")
# async def read_items(
#     q: Union[str, None] = None
# ):
#     results = {"items" : [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results

# 6.2 Query Paramater and String Validations (Additional Validation)
# @app.get("/items")
# async def read_items(
#     q: Annotated[Union[str, None], Query(max_length=10)] = None
# ):
#     results = {"items": [{"item_id": "foo"}, {"item_id": "bar"}]}
#     if q:
#         results.update({"q": q})
#     return results

# 7. Body - Multiple Parameter
# 7.1 Mix Path, Query and Body Parameters

# class Item(BaseModel):
#     name: str
#     description: Union[str, None] = None
#     price: float
#     tax: Union[float, None] = None
    
# @app.put("/items/{item_id}")
# async def update_item(
#     item_id: Annotated[int, Path(title="the ID of the Item to get", ge=0, le=1000)],
#     q: Union[str, None] = None,
#     item: Union[Item, None] = None
# ):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     if item:
#         results.update({"item": item})
#     return results

# 7.3 Multiple Body Paramater

# class Item(BaseModel):
#     name: str
#     description: Union[str, None] = None
#     price: float
#     tax: Union[float, None] = None
    
# class User(BaseModel):
#     username: str
#     full_name: Union[str, None] = None

# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item, user: User):
#     results = {"item_id": item_id, "item": item, "user": user}
#     return results

# 8. Body Fields
# class Item(BaseModel):
#     name: str
#     description: Union[str, None] = Field(
#         default=None, title="The descprtion of the item", max_length=300
#     )
#     price: float = Field(gt=0, description="The price mus be greater than zero")
#     tax: Union[float, None] = None
    
# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Annotated[Item, Body(embed=True)]):
#     results = {"item_id": item_id, "item": item}
#     return results

# 9. Body Nasted Models

# class Image(BaseModel):
#     url: HttpUrl
#     name: str

# class Item(BaseModel):
#     name: str
#     description: Union[str, None] = None
#     price: float
#     tax: Union[float, None] = None
#     tags: List[str] = []
#     images: Union[List[Image], None] = None
    
# class Offer(BaseModel):
#     name: str
#     description: Union[str, None] = None
#     price: float
#     items: List[Item]

# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item):
#     results = {"item_id": item_id, "item": item}
#     return results

# @app.post("/offers/")
# async def create_offer(offer: Offer):
#     return offer

# 10. Declare Request Example Data

# class Item(BaseModel):
#     name: str
#     description: Union[str, None] = None
#     price: float
#     tax: Union[float, None] = None
    
#     # model_config = {
#     #     "json_schema_extra": {
#     #         "example": 
#     #             {
#     #                 "name": "Sabun",
#     #                 "description": "Sabun adalah sesuatu yang bisa membuat kamu bahagia",
#     #                 "price": 20000.0,
#     #                 "tax": 2000.0
#     #             }
            
#     #     }
#     # }
    
# @app.put("/items/{item_id}")
# async def update_item(
#     *,
#     item_id: int, 
#     item: Annotated[
#         Item, 
#         Body(
#             example={
#                 "name": "Sabun",
#                 "description": "Sabun adalah sesuatu yang bisa membuat kamu bahagia",
#                 "price": 20000.0,
#                 "tax": 2000.0
#             }
#         )
#         ]
#     ):
#     results = {"item_id": item_id, "item": item}
#     return results

# 11. Cookie Paramaters

# @app.get("/items/")
# async def read_items(ads_id: Annotated[Union[str, None], Cookie()] = None):
#     return {"ads_id": ads_id}

# 12. Header Paramaters

# @app.get("/items/")
# async def read_items(user_agent: Annotated[Union[str, None], Header()] = None):
#     return {"User-Agent": user_agent}

# 13. Response Model - Return Type

# class Item(BaseModel):
#     name: str
#     description: Union[str, None] = None
#     price: float
#     tax: Union[float, None] = None
#     tags: List[str] = []

# @app.post("/items/")
# async def create_item(item: Item) -> Item:
#     return item

# @app.get("/items/")
# async def read_items() -> List[Item]:
#     return [
#         Item(name="Portal Gun", price= 20000.0),
#         Item(name="Plumbus", price=200.0)
#     ]

# 13.1 Response Model with Prior

# class UserIn(BaseModel):
#     username: str
#     password: str
#     email: EmailStr
#     full_name: Union[str, None] = None
    
# class UserOut(BaseModel):
#     username: str
#     email: EmailStr
#     full_name: Union[str, None] = None
    
# @app.post("/user/", response_model=UserOut)
# async def create_user(user: UserIn) -> Any:
#     return user

# 14. Form Data

# @app.post("/login/")
# async def login(username: Annotated[str, Form()], password: Annotated[str, Form()]):
#     return {"username": username}

# 15. Request File
# @app.post("/files/")
# async def create_file(file: Annotated[bytes, File()]):
#     return {"file_size": len(file)}

# @app.post("/uploadfiles/")
# async def create_upload_file(file: UploadFile, description: Annotated[str, Form()] = None):
#     return {"file_name": file.filename, "description": description}

# 16. Handling Errors

# items = [
#     {"foo": "The foo is the best"},
#     {"bar": "The bar is the best"}
# ]

# @app.get("/items/{item_id}")
# async def read_item(item_id: str):
#     for item in items:
#         key = next(iter(item))
#         if key != item_id:
#             raise HTTPException(status_code=404, detail="Item not found")
#         return item
    
# 17. Databases

            




@app_two.get("/")
async def root():
    return {"message": "Selamat Datang di API 2"}