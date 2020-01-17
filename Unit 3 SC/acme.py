# Importing the random library for use in the Product class
import random


class Product():
    '''
    This class is created for the purpose of product organization at the
    Acme Corporation.
    '''

    def __init__(self, name, price=10, weight=20, flammability=0.5,
                 identifier=random.randint(1000000, 9999999)):
        '''
        Constructor method that initiats self along with defining
        class variables takes in the following parameters: name,
        price, weight, flammability, identifier
        '''
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    def stealability(self):
        '''
        this methode calculates the price divided by its weight to
        determine weither a given product is not sealable, kinda
        stealable, or very stealable
        '''
        steal_factor = self.price/self.weight

        if steal_factor < 0.5:
            a = 'Not so stealable'
            print(a)
            return a
        elif steal_factor < 1:
            b = 'Kinda stealable'
            print(b)
            return b
        else:
            c = 'Very stealable!'
            print(c)
            return c

    def explode(self):
        '''
        this medhode returns the explode factor of a given Product
        this is determined by the flammability attribute times the
        weight attibute
        '''
        flame_factor = self.flammability*self.weight

        if flame_factor < 10:
            a = '...fizzle.'
            print(a)
            return a
        elif flame_factor < 50:
            b = '...boom!'
            print(b)
            return b
        else:
            c = '...BABOOM!!'
            print(c)
            return c


class BoxingGlove(Product):
    '''
    This is a sub class of the product class
    '''
    def __init__(self, name, price=10, weight=10, flammability=0.5,
                 identifier=random.randint(1000000, 9999999)):
        '''
        constructor methode
        '''
        Product.__init__(self, name, price=10, weight=10, flammability=0.5,
                         identifier=random.randint(1000000, 9999999))

    def explode(self):
        '''
        specife method for exploding gloves
        '''
        print("...it's a glove.")

    def punch(self):
        '''
        method that determints punch pain based off of glove weight
        '''
        if self.weight < 5:
            print('That tickles.')
        elif self.weight < 15:
            print('Hey that hurt!')
        else:
            print('OUCH!')
