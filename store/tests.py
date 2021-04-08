from django.test import TestCase
from store.models.customer import Customer
from store.models.Customer_form import Contact1

# Create your tests here.
class Basictest(TestCase):
    #def setUp(self):
    #    self.blog=Customer.objects.create(first_name='abc',last_name='cde',phone='1234567892',dob='2021-04-01',email='abc@gmail.com',password='123456')
    
    #def test_model(self):
    #    d=self.blog
    #    self.assertTrue(isinstance(d, Customer))
    #    self.assertEqual(str(d), 'abc')

    def Contact1(self):
        self.blog= Contact1.objects.create(Relation = 'Brother', name='hetal', dob='09/12/1992' , category='Mobiles' , customer= '24')
    def test_contact_module(self):
        e=self.blog
        self.assertTrue(isinstance(e, Contact1 ))
        self.assertEqual(str(e), 'Brother')

        