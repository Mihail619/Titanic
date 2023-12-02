from fastapi import FastAPI
from typing import List
from model.model import change_ticket_name, predictions
from .schemas import User, User_ticket


data = {
    "pclass": 2,
    "sex": "male",
    "age": 5,
    "sibsp": 5,
    "parch": 2,
    "fare": 425,
    "cabin": "C85",
    "embarked": "S",
    "deck": "C",
    "title": "Mr",
    "ticket_name": "PC 17599",
}


request_data = {}

fake_users = [
    {"id": 1, "role": "admin", "name": "Bob"},
    {"id": 2, "role": "client", "name": "John"},
    {"id": 3, "role": "client", "name": "Matt"},
    # {"id": 4, "role": "client", "name": "Homer", "degree": [
    #     {"id": 1, "created_at": "2020-01-01T00:00:00", "type_degree": "expert"}
    # ]},
]


app = FastAPI(title="Titanic preds")


@app.get("/")
def main():
    return "Hello this is the app that predicts would you survived on Titanic or not"


@app.get("/users/{user_id}", response_model=List[User])
def get_user(user_id: int):
    return [user for user in fake_users if user.get("id") == user_id]

@app.post("/user_preds")
def get_ticket_info(insert: User_ticket):
    request_data["Pclass"] = insert.pclass
    request_data["Sex"] = insert.sex
    request_data["Age"] = insert.age
    request_data["SibSp"] = insert.sibsp
    request_data["Parch"] = insert.parch
    request_data["Fare"] = insert.fare
    request_data["Cabin"] = insert.cabin
    request_data["Embarked"] = insert.embarked
    request_data["Deck"] = insert.deck
    request_data["Title"] = str(insert.title)
    request_data["New_ticket"] = change_ticket_name(insert.ticket_name)

    result = round(predictions(request_data), 3)
    return {
        "status": 200,
        "data": f"Ваши данные получены. Ваша вероятность выжить составляет: {result}"
    }
