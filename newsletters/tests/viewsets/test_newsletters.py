from rest_framework.test import APITestCase
from newsletters.models import Newsletter, Tags

class NewsletterApiTestCase(APITestCase):
    def setUp(self):
        self.newsletter = Newsletter.objects.create(name='Nuevo', description = 'Decription')
        self.tag = Tags.objects.create(name='Tag')
        self.newsletter.tags.add(self.tag)

    def test_retrieve_newsletter(self):
        result = self.client.get('/api/v1/newsletters/{0}/'.format(self.newsletter))
        assert result.status_code == 200
        assert result.data['name'] == self.newsletter.name

    def test_list_newsletter(self):
        result = self.client.get('/api/v1/newsletters')
        assert result.status_code == 200
        assert result.data['count'] == 1

    def test_get_newsletter_tags(self):
        result = self.client.get('/api/v1/newsletters/{0}/tags/'.format(self.newsletter))
        assert result.status_code == 200
        assert result.data['count'] == 1
        assert result.data['results'][0]['name'] == self.tag.name
