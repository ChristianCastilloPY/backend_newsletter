from rest_framework.test import APITestCase
from django.contrib.auth.models import User

class UsersApiTestCase(APITestCase):
    def test_create_user(self):
        user_data = {
            'username': 'usernamel',
            'email': 'usernamel@gmail.com',
            'password' : '123456'
        }

        result = self.client.post('/api/v1/users', user_data)

        assert result.status_code == 201