from django.urls import include, path
from rest_framework import routers
from core.views import UserViewSet
from newsletters.views import NewsletterViewSets, TagsViewSets

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'newsletters', NewsletterViewSets)
router.register(r'tag', TagsViewSets)


urlpatterns = [
    path('', include(router.urls),)
]