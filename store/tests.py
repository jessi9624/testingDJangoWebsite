from django.test import TestCase
from store.models.customer import Customer

# Create your tests here.
class Basictest(TestCase):
    def setUp(self):
        self.blog=Customer.objects.create(first_name='abc',last_name='cde',phone='1234567892',dob='2021-04-01',email='abc@gmail.com',password='123456')
    
    def test_model(self):
        d=self.blog
        self.assertTrue(isinstance(d,Customer))
        self.assertEqual(str(d))
        