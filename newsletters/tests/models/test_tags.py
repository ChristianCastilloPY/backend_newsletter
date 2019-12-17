from django.utils.text import slugify
from rest_framework.test import APITestCase

from newsletter.newsletters.models import Tags


class TagModelApiTestCase(APITestCase):
    def test_tag_model_slug(self):
        name = 'Prueba slug'
        tag = Tags.objects.create(name=name)

        assert tag.slug == slugify(name)