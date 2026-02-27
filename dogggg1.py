class DogStore:
    def __init__(self):
        self.products = []
        self.total_money = 0
    def add_food(self, name, price, weight):
        if price > 0:
            if weight > 0:
                self.products.append({
                    "type": "food",
                    "name": name,
                    "price": price,
                    "weight": weight
                })
    def add_toy(self, name, price, size):
        if price > 0:
            if size in ["S", "M", "L"]:
                self.products.append({
                    "type": "toy",
                    "name": name,
                    "price": price,
                    "size": size
                })
    def calculate_discount(self, age):
        if age < 1:
            return 0.2
        if age > 10:
            return 0.15
        return 0
    def checkout(self, age):
        total = 0
        for product in self.products:
            total += product["price"]
        discount = self.calculate_discount(age)
        total = total - (total * discount)
        if total > 1000:
            total = total - 100  # магічне число
        self.total_money += total
        self.products = []
        return total
    def get_dog_category(self, age):
        if age < 1:
            return "puppy"
        if age >= 1 and age <= 7:
            return "adult"
        if age > 7:
            return "senior"