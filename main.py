import uvicorn
from fastapi import FastAPI


from data import User, users

app = FastAPI()

def username_uniqueness_check(username: str):
    global users
    return username in [ user.username for user in users ]

def remove_user(username: str):
    global users
    users = [user for user in users if user.username != username]

def get_user(username: str):
    global users
    for user in users:
        if user.username == username:
            return user
    return None

@app.get("/user/{username}")
async def get_users_by_username(username: str):
    user = get_user(username)
    if user == None:
        return {"error": f'User "{username}" does not exist'}
    return user

@app.get("/users")
async def get_all_users(limit: int = 5):
    if limit < 0:
        return {"error": "limit can not be a negative number."}
    return users[:limit]

@app.post("/user")
async def create_user(user: User):
    global users
    if username_uniqueness_check(user.username):
        return {"error": f'The username "{user.username}" is taken.'}
    users.append(user)
    return user

@app.delete("/user/{username}")
async def delete_user(username: str):
    global users
    if username_uniqueness_check(username):
        remove_user(username)
        return {"message": "success"}
    else:
        return {"error": f'user "{username}" does not exist.'}


@app.put("/user/{username}")
async def modify_user(username: str, user: User):
    global users
    if username_uniqueness_check(user.username):
        remove_user(user.username)
        users.append(user)
        return user
    elif user.username != username:
        return {"error": f'username provided in the rest param is not macthing the request body.'}
    else:
        return {"error": f'user "{User.username}" does not exist.'}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8920)