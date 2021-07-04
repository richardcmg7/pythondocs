from unittest import TestCase
from experts_admin import ExpertsSelected
from expert import Expert


class TestExpertsSelected(TestCase):
    def test_email_input(self):
        self.fail()

    def test_id_input(self):
        self.fail()

    def test_get_experts_selected(self):
        selected = ExpertsSelected()
        expert = selected.select_expert()
        print(expert)
        self.assertEqual(type(expert[0]), Expert)

    def test_select_expert(self):
        selected = ExpertsSelected()
        expert = selected.select_expert()
        self.assertEqual(type(expert[0]), Expert)

    def test_add_expert(self):
        selected = ExpertsSelected()
        expert = selected.select_expert()

