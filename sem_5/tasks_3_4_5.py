import uvicorn as uvicorn
from pydantic import BaseModel
from fastapi import FastAPI, Request, HTTPException, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles


class User(BaseModel):
    id: int
    name: str
    email: str
    password: str


users = []
for i in range(10):
    users.append(
        User(
            id=i + 1, name=f"name{i + 1}", email=f"email{i + 1}@mail.ru", password="123"
        )
    )

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/users/", response_class=HTMLResponse)
def get_users(request: Request):
    return templates.TemplateResponse(
        "user.html", {"request": request, "users": users}
    )


@app.post("/users/", response_class=HTMLResponse)
def del_users(request: Request, user_id: int = Form(...)):
    for user in users:
        if user.id == user_id:
            users.remove(user)
            break
    return templates.TemplateResponse(
        "user.html", {"request": request, "users": users}
    )


@app.get("/users/add", response_class=HTMLResponse)
def add_users_form(request: Request):
    return templates.TemplateResponse("add_users_form.html", {"request": request})


@app.put("/users/", response_class=HTMLResponse)
async def edit_users(user_id: int, new_user: User):
    for i in range(0, len(users)):
        if users[i].id == user_id:
            current_user = users[user_id - 1]
            current_user.name = new_user.name
            current_user.email = new_user.email
            current_user.password = new_user.password
            return current_user
    raise HTTPException(status_code=404, detail="Task not found")


@app.post("/process_form")
async def process_form(request: Request):
    data_form = await request.form()
    name = data_form.get("name")
    email = data_form.get("email")
    password = data_form.get("password")
    users.append(User(id=len(users) + 1, name=name, email=email, password=password))
    return templates.TemplateResponse("success_add.html", {"request": request})


if __name__ == "__main__":
    uvicorn.run("tasks_3_4_5:app", host="127.0.0.1", port=8000, reload=True)
