import json
from enum import Enum
from datetime import datetime
from typing import Optional, List


class Name(Enum):
    EXTRA = "Extra"
    PÃO_DE_AÇÚCAR = "Pão de Açúcar"
    SONDA = "Sonda"


class Merchant:
    image: str
    name: Name
    price: str
    last_update: datetime

    def __init__(self, image: str, name: Name, price: str, last_update: datetime) -> None:
        self.image = image
        self.name = name
        self.price = price
        self.last_update = last_update


class URL(Enum):
    ALIMENTOS = "alimentos"


class Metadata:
    department_url: URL
    subdepartment_url: str

    def __init__(self, department_url: URL, subdepartment_url: str) -> None:
        self.department_url = department_url
        self.subdepartment_url = subdepartment_url


class Product:
    id: int
    url: str
    name: str
    image: str
    price: str
    metadata: Metadata
    saving_percentage: Optional[str]
    cart_quantity: int
    max_cart_quantity: int
    paused: bool
    merchants: List[Merchant]

    def __init__(self, id: int, url: str, name: str, image: str, price: str, metadata: Metadata, saving_percentage: Optional[str], cart_quantity: int, max_cart_quantity: int, paused: bool, merchants: List[Merchant]) -> None:
        self.id = id
        self.url = url
        self.name = name
        self.image = image
        self.price = price
        self.metadata = metadata
        self.saving_percentage = saving_percentage
        self.cart_quantity = cart_quantity
        self.max_cart_quantity = max_cart_quantity
        self.paused = paused
        self.merchants = merchants


class Subdepartment:
    id: int
    url: str
    name: str
    last: bool
    products: List[Product]

    def __init__(self, id: int, url: str, name: str, last: bool, products: List[Product]) -> None:
        self.id = id
        self.url = url
        self.name = name
        self.last = last
        self.products = products


class Shopper:
    title: str
    url: URL
    subdepartments: List[Subdepartment]

    def __init__(self, title: str, url: URL, subdepartments: List[Subdepartment]) -> None:
        self.title = title
        self.url = url
        self.subdepartments = subdepartments

    @classmethod
    def from_json(cls, json_string):
        json_dictionary = json.loads(json_string)
        return cls(**json_dictionary)
