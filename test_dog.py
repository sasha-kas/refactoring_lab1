import pytest
from dogggg1 import DogStore

def test_add_food():
    store = DogStore()
    store.add_food("Premium Food", 500, 2)
    assert len(store.products) == 1

def test_add_food_negative_price():
    store = DogStore()
    store.add_food("Cheap Food", -100, 2)
    assert len(store.products) == 0

def test_add_toy():
    store = DogStore()
    store.add_toy("Ball", 200, "M")
    assert len(store.products) == 1

def test_invalid_toy_size():
    store = DogStore()
    store.add_toy("Ball", 200, "XL")
    assert len(store.products) == 0

def test_puppy_discount():
    store = DogStore()
    assert store.calculate_discount(0) == 0.2

def test_senior_discount():
    store = DogStore()
    assert store.calculate_discount(12) == 0.15

def test_adult_discount():
    store = DogStore()
    assert store.calculate_discount(5) == 0

def test_checkout_without_discount():
    store = DogStore()
    store.add_food("Food", 500, 2)
    total = store.checkout(5)
    assert total == 500

def test_checkout_with_puppy_discount():
    store = DogStore()
    store.add_food("Food", 1000, 2)
    total = store.checkout(0)
    assert total == 800  # 20% знижка

def test_big_order_bonus_discount():
    store = DogStore()
    store.add_food("Food", 1100, 2)
    total = store.checkout(5)
    assert total == 1000  # 1100 - 100