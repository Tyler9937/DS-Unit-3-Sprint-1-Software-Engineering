# Importing needed library and Product class
import random
from acme import Product

# creating lists of adjectives and nouns
adjectives = ['Cool', 'Flavorful', 'Shiny', 'Awsome']
nouns = ['Phone', 'PS4', 'Computer', 'Anvil']


def generate_products(num_products=30):
    '''
    creates a list of products given the num_products input and the
    adjectives and nouns lists
    '''
    products = []
    for i in range(0, num_products):
        name = adjectives[random.randint(0, len(adjectives)-1)] + ' ' + nouns[random.randint(0, len(nouns)-1)]
        price = random.randint(5, 100)
        weight = random.randint(5, 100)
        flammability = random.uniform(0.0, 2.5)
        products.append(Product(name=name, price=price, weight=weight, flammability=flammability))

    return products

generate_products()

def inventory_report(products):
    '''
    takes a list of products input and outputs a nice summery
    '''
    price_list = []
    weight_list = []
    flame_list = []

    for obj in products:
        price_list.append(obj.price)
        weight_list.append(obj.weight)
        flame_list.append(obj.flammability)

        average_price = sum(price_list) / len(price_list)
        average_weight = sum(weight_list) / len(weight_list)
        average_flame = sum(flame_list) / len(flame_list)


    print('ACME CORPORATION OFFICIAL INVENTORY REPORT')
    print('Unique product names: ' + str(len(products)))
    print('Average price: {}'.format(average_price))
    print('Average weight: {}'.format(average_weight))
    print('Average flammability: {}'.format(average_flame))


if __name__ == '__main__':
    inventory_report(generate_products())
