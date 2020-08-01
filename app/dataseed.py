from django_seed import Seed
from .food_prices.models import Country


def seed():
    items = ["pork", "chicken", "beef"]
    for m in range(3):
        seeder = Seed.seeder()
        item = items[m]
        for i in range(3):
            seeder.add_entity(Country, 1, {"item": item})
        seeder.execute()
    print(f"Seeded")


seed()
