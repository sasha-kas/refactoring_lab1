from dataclasses import dataclass
from typing import List

#-магічні числа:)
PUPPY_AGE_LIMIT = 1
ADULT_AGE_LIMIT = 7
SENIOR_AGE_LIMIT = 10

PUPPY_DISCOUNT = 0.20
SENIOR_DISCOUNT = 0.15

BIG_ORDER_THRESHOLD = 1000
BIG_ORDER_BONUS = 100

@dataclass
class Product:
    name: str
    price: float

    def validate_price(self):
        if self.price <= 0:
            raise ValueError("Price must be positive")

@dataclass
class Food(Product):
    weight: float

    def __post_init__(self):
        self.validate_price()
        if self.weight <= 0:
            raise ValueError("Weight must be positive")

@dataclass
class Toy(Product):
    size: str
    ALLOWED_SIZES = {"S", "M", "L"}

    def __post_init__(self):
        self.validate_price()
        if self.size not in self.ALLOWED_SIZES:
            raise ValueError("Invalid toy size")

class DiscountService:

    @staticmethod
    def calculate(age: int) -> float:
        if age < PUPPY_AGE_LIMIT:
            return PUPPY_DISCOUNT
        if age > SENIOR_AGE_LIMIT:
            return SENIOR_DISCOUNT
        return 0

class DogCategoryService:

    @staticmethod
    def get_category(age: int) -> str:
        if age < PUPPY_AGE_LIMIT:
            return "puppy"
        elif age <= ADULT_AGE_LIMIT:
            return "adult"
        else:
            return "senior"

class DogShop:

    def __init__(self):
        self.products: List[Product] = []
        self.total_income = 0

    def add_product(self, product: Product):
        self.products.append(product)

    def calculate_total(self, age: int) -> float:
        total = sum(product.price for product in self.products)

        discount = DiscountService.calculate(age)
        total -= total * discount

        if total > BIG_ORDER_THRESHOLD:
            total -= BIG_ORDER_BONUS

        return total

    def checkout(self, age: int) -> float:
        total = self.calculate_total(age)
        self.total_income += total
        self.products.clear()
        return total