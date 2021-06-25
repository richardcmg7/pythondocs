from unittest import TestCase
from src.talents.talent_book import TalentBook


class Test(TestCase):
    def test_talent_book(self):
        talents = TalentBook
        talents.add(self, "name", "email", "phone", "identity", "id_city")

