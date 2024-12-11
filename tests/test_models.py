import unittest

from django.contrib.auth import get_user_model

from taxi.models import Manufacturer, Driver, Car


class TestModels(unittest.TestCase):
    def test_manufacturer_str(self):
        manufacturer = Manufacturer.objects.create(name="test",
                                                   country="test_country")
        self.assertEqual(str(manufacturer),
                         f"{manufacturer.name} {manufacturer.country}")

    def test_driver_str(self):
        username = "Jacky"
        password = "<PASSWORD>"
        first_name = "Jack"
        last_name = "Doe"
        driver = get_user_model().objects.create(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name)
        self.assertEqual(str(driver),
                         f"{username} ({first_name} {last_name})")

    def test_car_str(self):
        manufacturer = Manufacturer.objects.create(name="test",
                                                   country="test_country")
        car = Car.objects.create(model="test_model", manufacturer=manufacturer)
        self.assertEqual(str(car),
                         f"{manufacturer.name} {manufacturer.country}")
