from django.test import TestCase
from stores.factories import StoreFactory
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
from stores.models import Store

class StoreTestCase(TestCase):
    def test_optional_fields_succeed(self):
        store = StoreFactory(
            name="Backwerk Bakery",
            address="Harkotstrasse 23, Dortmund, 44227",
            is_open=True,
        )
        self.assertEqual(store.name, "Backwerk Bakery")
        self.assertEqual(store.address, "Harkotstrasse 23, Dortmund, 44227")
        self.assertEqual(store.is_open, True)

    def test_null_name_fails(self):
        with self.assertRaises(IntegrityError):
            Store.objects.create(name=None, address='Address 134, 44789')

    def test_create_store(self):
        # Create a store instance
        store = Store.objects.create(
            name="Test Bakery",
            address="Test Address, Test City, 12345",
            is_open=True,
        )
        # Retrieve the store from the database
        stored_store = Store.objects.get(name="Test Bakery")
        self.assertEqual(store, stored_store)

    def test_blank_address(self):
        # Create a store without an address
        store = StoreFactory(address="", is_open=True)
        self.assertEqual(store.address, "")

    def test_is_open_default_value(self):
        # Create a store without specifying 'is_open', should default to True
        store = StoreFactory(name="Default Open Bakery", address="Default Address")
        self.assertEqual(store.is_open, True)


