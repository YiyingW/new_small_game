from django.test import TestCase
from django.urls import resolve
from django.urls import reverse
from .views import index, detail

# Create your tests here.

class IndexTests(TestCase):

    def setUp(self):
        url = reverse('games:index')
        self.response = self.client.get(url)

    def test_index_view_status_code(self): 
        self.assertEquals(self.response.status_code, 200)

    def test_index_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func, index)


class DetailTests(TestCase):

    def test_detail_game0_status_code(self):
        url = reverse('detail', args=['0'])
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_detail_game1_status_code(self):
        url = reverse('detail', args=['1'])
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_detail_url_resolves_game0_view(self):
        view = resolve('/0/')
        self.assertEquals(view.func, detail)

    def test_detail_url_resolves_game1_view(self):
        view = resolve('/1/')
        self.assertEquals(view.func, detail)

    def test_detail_url_resolves_game2_view(self):
        view = resolve('/2/')
        self.assertEquals(view.func, detail)
