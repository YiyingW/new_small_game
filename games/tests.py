from django.test import TestCase
from django.urls import resolve
from django.urls import reverse
from .views import index, detail, summary
from .forms import GameForm
from .models import History

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

    def test_detail_url_resolves_game_view(self):
        view = resolve('/0/')
        self.assertEquals(view.func, detail)

    def test_detail_view_contains_link_to_index_page(self):
        game_url = reverse('detail', args=['0'])
        response = self.client.get(game_url)
        index_url = reverse('games:index')
        self.assertContains(response, 'href="{0}"'.format(index_url))

class SummaryTests(TestCase):

    def test_summary_view_status_code(self):
        url = reverse('summary')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_summary_url_resolves_summary_view(self):
        view = resolve('/summary/')
        self.assertEquals(view.func, summary)

    def test_summary_view_contains_link_to_index_page(self):
        summary_url = reverse('summary')
        response = self.client.get(summary_url)
        index_url = reverse('games:index')
        self.assertContains(response, 'href="{0}"'.format(index_url))

class GameFormTests(TestCase):

    def test_new_user_comment_valid_post_data(self):
        url = reverse('detail', kwargs={'game_id': '0'})
        data = {
            'player_name' : "Xiao Mao",
            'comment': "Fun game"
        }
        response =  self.client.post(url, data)
        self.assertTrue(History.objects.exists())



