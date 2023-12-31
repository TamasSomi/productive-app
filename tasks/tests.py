from django.contrib.auth.models import User
from .models import Task
from rest_framework import status
from rest_framework.test import APITestCase


class TaskListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='tomi', password='pass')

    def test_can_list_tasks(self):
        tomi = User.objects.get(username='tomi')
        Task.objects.create(owner=tomi, title='a title')
        response = self.client.get('/tasks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        print(len(response.data))

    def test_logged_in_user_can_create_task(self):
        self.client.login(username='tomi', password='pass')
        response = self.client.post('/tasks/', {'title': 'a title'})
        count = Task.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_not_logged_in_cant_create_task(self):
        response = self.client.post('/tasks/', {'title': 'a title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class TestDetailViewTests(APITestCase):
    def setUp(self):
        tomi = User.objects.create_user(username='tomi', password='pass')
        george = User.objects.create_user(username='george', password='pass')
        Task.objects.create(
            owner=tomi, title='a title', content='tomis content'
        )
        Task.objects.create(
            owner=george, title='another title', content='georges content'
        )

    def test_can_retrieve_task_using_valid_id(self):
        response = self.client.get('/tasks/1/')
        self.assertEqual(response.data['title'], 'a title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cant_retrieve_task_using_invalid_id(self):
        response = self.client.get('/tasks/966')
        self.assertEqual(
            response.status_code, status.HTTP_301_MOVED_PERMANENTLY
        )
