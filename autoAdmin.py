"""Defining all the process that required for admin and automate those"""
from FruitBasket import db
from FruitBasket.scraper import image_spider
from FruitBasket.model import Products
import random

# First of all I need to define all the process that a admin can do.
# Defining the role of image spider.
input_field = str(input('Provide the name of the product:\n> '))
print("Getting data.....")
product_data = image_spider(input_field=input_field)


def admin_process(input_data):  # For adding products
    for i in range(len(input_data[0])):
        a = random.randint(1, 10)
        b = random.randint(11, 1000)
        product_id = random.randint(a, b)
        if db.session.query(Products).filter_by(productId=product_id).count() < 1:
            product = Products(productId=product_id,
                               productName=input_data[1][i],
                               stocks=random.randint(50, 100), price=random.randint(20, 80),
                               description="""Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eos laborum nihil
                                perferendis reiciendis sint. Facilis fuga quidem sint totam voluptates. Cum deserunt
                                doloribus enim error impedit, labore maxime nam quia.""",
                               offer=str(random.randint(10, 20)) + "% off",
                               image_url=input_data[0][i])

            db.session.add(product)
            db.session.commit()
        else:
            continue


admin_process(product_data)
print("Done")
# And Done
