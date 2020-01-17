# importing unittest and class and files from loco repo
import unittest
from acme import Product
from acme_report import generate_products, adjectives, nouns


class AcmeProductTests(unittest.TestCase):
    """
    Testing if Acme products are acceptable
    """

    def test_default_product_price(self):
        """
        testing test that price defult is 10
        """
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)
        self.assertEqual(prod.weight, 20)

    def test_apples(self):
        '''
        tests apples product
        '''
        prod2 = Product('apples', price=60, weight=30, flammability=.04)

        self.assertEqual(prod2.stealability(), 'Very stealable!')
        self.assertEqual(prod2.explode(), '...fizzle.')


class AcmeReportTests(unittest.TestCase):
    '''
    Testing reports of acme products
    '''

    def test_default_num_products(self):
        '''
        check if num_products lenth
        '''
        self.assertEqual(len(generate_products()), 30)

    def test_legal_names(self):
        '''
        test for legal name, splits to check for space
        then calls each string in list to see if it contains a
        adjective or noun
        '''
        test = generate_products()
        test = test[0].name.split(' ')
        self.assertIn(test[0], adjectives+nouns)
        self.assertIn(test[1], adjectives+nouns)

if __name__ == '__main__':
    unittest.main()
