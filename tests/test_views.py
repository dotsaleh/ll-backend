from django.test import TestCase
from restaurant.models import Menu
from restaurant.views import MenuItemView
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="Donout", price=2, inventory=1)
        Menu.objects.create(title="Eclair", price=12, inventory=2)
    
    def test_getall(self):
        items = Menu.objects.all()
        serialized = []
        for item in items:
            serialized.append(MenuSerializer(item))
            print(item)
            
        
