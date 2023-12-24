from catboost import CatBoostClassifier
import pandas as pd
import numpy as np

model = CatBoostClassifier()

# model.load_model("model_4")
model.load_model("model/model_4")

data = pd.read_csv("model/processed_data.csv", nrows=3)
data.drop("Survived", axis=1, inplace=True)


def change_ticket_name(ticket_name):
    '''Ф-я преобразовывает название билета в новую колонку'''
    # data["New_ticket"] = data['Ticket'].apply(lambda x: 1 if any(char.isalpha() for char in x) else 0)
    new_ticket = 1 if ticket_name.isalpha() else 0
    return new_ticket


def predictions(input_data):
    '''Ф-я, которая делает предсказания вероятности выжить
    на основе входящих данных'''
    # print(type(input_data))
    
    X = list(input_data.values())
    
    positive_preds = model.predict_proba(X)[1]
    
    return positive_preds

def get_cabin(deck, cabin_number):
    return deck + cabin_number


if __name__ == "__main__":
    input = {
        "Pclass": 2,
        "Sex": "male",
        "Age": 5,
        "SibSp": 5,
        "Parch": 2,
        "Fare": 5425,
        "Cabin": "C85",
        "Embarked": "S",
        "Deck": "C",
        "Title": "Mr",
        "New_ticket": 1,
    }
    
    # print(predictions(input))
