from pydantic import BaseModel, Field
from enum import Enum


class User(BaseModel):
    id: int
    role: str
    name: str


class Title(Enum):
    mr = "Mr"
    mrs = "Mrs"
    miss = "Miss"
    master = "Master"
    don = "Don"
    rev = "Rev"
    dr = "Dr"
    mme = "Mme"
    ms = "Ms"
    major = "Major"
    lady = "Lady"
    sir = "Sir"
    mille = "Mlle"
    col = "Col"
    capt = "Capt"
    countess = "the Countess"
    jonkheer = "Jonkheer"


class User_ticket(BaseModel):
    pclass: int = Field(ge=1, le=3)  # есть 3 класса: 1, 2, 3
    sex: str  # 2 пола: "male", "female"
    age: int = Field(ge=0, lt=120)  # возраст
    sibsp: int = Field(ge=0)  # количество родственников
    parch: int  # количество детей или родителей
    fare: int = Field(ge=0, lt=513)  # стоимость билета > 0  513<
    cabin: str  # название номера. включает в себя название палубы и порядковый номер ('C123')
    embarked: str  # место посадки. есть (S, C, Q)
    deck: str  # название палубы: 'A' 'B' 'C' 'D' 'E' 'F' 'G' 'T'
    title: Title  # титул
    ticket_name: str  # Назкание билета: "PC 17599", "STON/O2. 3101282", "113803".
    # Из этого параметра определяется есть ли в названии билета буквы: 1 - есть, 2-нет.