from catboost import CatBoostClassifier
import pandas as pd

model = CatBoostClassifier()

model.load_model("model\model_4")

data = pd.read_csv("model\processed_data.csv", nrows=3)
data.drop("Survived", axis=1, inplace=True)


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
X = input.values()
print(X)
# predictions = model.predict()