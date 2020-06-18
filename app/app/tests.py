from django.test import TestCase
from app.calc import add, subtract

# Command to execute the tests
# docker-compose run app sh -c "python manage.py test && flake8"


class CalcTests(TestCase):
    def test_add_numbers(self):
        """Test that two numbers are added together"""
        self.assertEqual(add(3, 8), 11)

    def test_subtract_numbers(self):
        """Test that values are subtracted and returned"""
        self.assertEqual(subtract(11, 5), 6)
