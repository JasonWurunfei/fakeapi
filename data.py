from pydantic import BaseModel

class User(BaseModel):
    username: str
    age: int

users = [
    User(**{
        "username": "Jason",
        "age": 15
    }),
    User(**{
        "username": "John",
        "age": 29
    }),
    User(**{
        "username": "张三",
        "age": 40
    }),
    User(**{
        "username": "李四",
        "age": 50
    }),
    User(**{
        "username": "Jack",
        "age": 32
    })
]

