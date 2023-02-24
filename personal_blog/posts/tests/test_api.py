import json

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from posts.models import Post
from posts.serializers import PostsSerializer


class PostApiTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username='test_user')
        self.client.force_login(self.user)
        self.post_1 = Post.objects.create(title='Test-1', content='test-1', author=self.user)
        self.post_2 = Post.objects.create(title='Test-2', content='test-2', author=self.user)

    def test_create(self):
        self.client.force_login(self.user)
        post_url = reverse('post-list')

        data = {
            'title': 'test-added',
            'content': 'test-added'
        }

        data_json = json.dumps(data)
        response = self.client.post(post_url, data=data_json, content_type='application/json')
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)

        get_url = reverse('post-detail', kwargs={'pk': response.data['id']})
        created_post = self.client.get(get_url)
        self.assertEqual(data['title'], created_post.data['title'])
        self.assertEqual(data['content'], created_post.data['content'])

        post_creator = User.objects.get(id=created_post.data['author'])
        self.assertEqual(self.user, post_creator)

    def test_update(self):
        self.client.force_login(self.user)
        patch_url = reverse('post-detail', args=(self.post_1.id, ))

        data = {
            'title': self.post_1.title,
            'content': 'test-updated'
        }

        data_json = json.dumps(data)
        response = self.client.patch(patch_url, data=data_json, content_type='application/json')
        self.assertEqual(status.HTTP_200_OK, response.status_code)

        get_url = reverse('post-detail', kwargs={'pk': self.post_1.id})
        updated_post = self.client.get(get_url)
        self.assertEqual(data['content'], updated_post.data['content'])

    def test_get(self):

        self.client.force_login(self.user)

        url = reverse('post-list')

        response = self.client.get(url)
        serializer_data = PostsSerializer([self.post_1, self.post_2], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(2, Post.objects.all().count())
        self.assertEqual(serializer_data, response.data)

    def test_delete(self):
        self.client.force_login(self.user)
        delete_url = reverse('post-detail', kwargs={'pk': self.post_1.id})
        self.client.delete(delete_url)
        deleted_post = self.client.get(delete_url)
        self.assertEqual(status.HTTP_404_NOT_FOUND, deleted_post.status_code)

    def test_searching(self):

        url = reverse('post-list')

        response = self.client.get(url, data={'search': 'test-1'})
        # print(response.data)
        serializer_data = PostsSerializer([self.post_1, ], many=True).data
        self.assertEqual(response.data, serializer_data)

    # def test_filtering(self):
    #
    #     another_user = User.objects.create(username='another_user')
    #     self.client.force_login(another_user)
    #     post_3 = Post.objects.create(author=another_user, title='Test-3', content='test-3')
    #     url = reverse('post-list')
    #
    #     response = self.client.get(url, data={'filter': {'author': another_user}})
    #     print(response.data)
    #     serializer_data = PostsSerializer([post_3, ], many=True).data
    #     self.assertEqual(response.data, serializer_data)

    # def test_update(self):
    #     self.client.force_login(self.user)
    #     url = reverst('')