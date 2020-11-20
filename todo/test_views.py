from django.test import TestCase
from .models import Item

# Create your tests here.


class TestViews(TestCase):

    # Testa as respostas HTTP às views. Usamos um built in
    # HTTP client que já vem com o Django testing framework
    def test_get_todo_list(self):
        # Criamos uma variável q define a resposta q deve aparecer
        response = self.client.get('/')
        # Para confirmar que a resposta é 200 (código p uma
        # successfull HTTP response)
        self.assertEqual(response.status_code, 200)
        # Para confirmar que a view usa o template correcto
        self.assertTemplateUsed(response, 'todo/todo_list.html')

    def test_get_add_item_page(self):
        response = self.client.get('/add')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/add_item.html')

    def test_get_edit_item_page(self):
        # Importamos o que precisamos (ver linha 2)
        # Criamos um item cujo ID possa ser usado neste teste
        # mas que seja genérico o suficiente p permitir passar o
        # teste sem dependermos do q está de facto criado na app.
        item = Item.objects.create(name='Test Todo Item')
        response = self.client.get(f'/edit/{item.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/edit_item.html')

    # a partir daqui as acções implicam adicionar alguma coisa na BD e
    # portanto usamos o método POST em vez de GET
    def test_can_add_item(self):
        response = self.client.post('/add', {'name': 'Test Added Item'})
        self.assertRedirects(response, '/')

    def test_can_delete_item(self):
        # P/ testar se conseguirmos delete um item, temos de criar primeiro um:
        item = Item.objects.create(name='Test Todo Item')
        response = self.client.get(f'/delete/{item.id}')
        self.assertRedirects(response, '/')
        # P/ confirmar que foi apagado:
        existing_items = Item.objects.filter(id=item.id)
        # Se successful, apagámos o único item que criámos p/ o teste, logo,
        # podemos fazer a verificação testando se o length é zero.
        self.assertEqual(len(existing_items), 0)

    def test_can_toggle_item(self):
        item = Item.objects.create(name='Test Todo Item', done=True)
        response = self.client.get(f'/toggle/{item.id}')
        self.assertRedirects(response, '/')
        updated_item = Item.objects.get(id=item.id)
        self.assertFalse(updated_item.done)

    def test_can_edit_item(self):
        item = Item.objects.create(name='Test Todo Item')
        response = self.client.post(f'/edit/{item.id}', {'name': 'Updated Name'})
        self.assertRedirects(response, '/')
        updated_item = Item.objects.get(id=item.id)
        self.assertEqual(updated_item.name, 'Updated Name')
