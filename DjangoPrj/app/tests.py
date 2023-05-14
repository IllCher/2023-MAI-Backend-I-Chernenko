from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Film, Director
from selenium import webdriver
from django.test import LiveServerTestCase
import time
import os
import traceback
import sys
from unittest.mock import patch
import factory


class DirectorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Director

    name = factory.Sequence(lambda n: f'Director {n}')


class FilmFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Film

    title = factory.Sequence(lambda n: f'Film {n}')
    year = factory.Sequence(lambda n: 2000 + n)

    @factory.post_generation
    def directors(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for director in extracted:
                self.directors.add(director)


class FilmTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.director = DirectorFactory()
        self.film = FilmFactory(directors=[self.director])

    def test_get_all_films(self):
        url = reverse('film-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], self.film.title)

    def test_create_film(self):
        url = reverse('create')
        data = {'title': 'The Dark Knight', 'year': 2008, 'director_name': 'Christopher Nolan'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(Film.objects.filter(title='The Dark Knight').exists())

    def test_search(self):
        FilmFactory(title='Star Wars', year=1977)
        FilmFactory(title='The Empire Strikes Back star', year=1980)
        FilmFactory(title='Return of the Jedi', year=1983)

        response = self.client.get('/api/search?query=star')

        self.assertEqual(response.status_code, 200)
        data = response.json()['data']
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0]['title'], 'Star Wars')
        self.assertEqual(data[0]['year'], 1977)
        self.assertEqual(data[1]['title'], 'The Empire Strikes Back star')
        self.assertEqual(data[1]['year'], 1980)

    # mock
    @patch('app.models.Film.objects.filter')
    def test_search_mock(self, mock_filter):
        mock_films = [Film(title='Star Wars', year=1977), Film(title='The Empire Strikes Back star', year=1980)]
        mock_filter.return_value = mock_films

        response = self.client.get('/api/search?query=star')

        self.assertEqual(response.status_code, 200)
        data = response.json()['data']
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0]['title'], 'Star Wars')
        self.assertEqual(data[0]['year'], 1977)
        self.assertEqual(data[1]['title'], 'The Empire Strikes Back star')
        self.assertEqual(data[1]['year'], 1980)


class HomePageTest(LiveServerTestCase):
    selenium = None

    def setUp(self):
        super().setUp()

        options = webdriver.ChromeOptions()
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--headless')

        self.selenium = webdriver.Chrome(options=options)
        self.selenium.implicitly_wait(2)

    def tearDown(self):
        self.selenium.quit()
        super().tearDown()

    def test_button_click(self):
        sys.tracebacklimit = 0

        self.selenium.get(self.live_server_url)

        sys.tracebacklimit = 1000

        button = self.selenium.find_element("xpath", "//button[text()='Click me']")
        button.click()
        time.sleep(1)
        button_text = button.text
        self.assertEqual(button_text, "Clicked")
