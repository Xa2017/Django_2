from django.test import TestCase
from recruit.clawer import recruit

# Create your tests here.


def test_animals_can_speak():
    """Animals that can speak are correctly identified"""
    recruit.run()


