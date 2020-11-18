from django.test import TestCase
from .forms import ItemForm


class TestItemForm(TestCase):

    def test_item_name_is_required(self):
        # Isto simula um user submeter um formulário sem ter preenchido o nome.
        form = ItemForm({'name': ''})
        # Como o formulário sem nome não deve ser válido, usamos o
        # "assertFalse" para garantir que é isto que se verifica.
        self.assertFalse(form.is_valid())
        # "assertIn" permite verificar se há uma key para o name no
        # nosso dicionário.
        self.assertIn('name', form.errors.keys())
        # Isto verifica se a mensagem de erro que é mostrada é igual a
        # 'This field is required.'
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_done_field_is_not_required(self):
        form = ItemForm({'name': 'Test Todo Item'})
        self.assertTrue(form.is_valid())

    # Isto testa se os fields do formulário que aparecem para o
    # user continuam a ser os mesmos que definimos no ficheiro forms.py
    def test_fields_are_explicit_in_form_metaclass(self):
        form = ItemForm()
        self.assertEqual(form.Meta.fields, ['name', 'done'])
