from rest_framework import serializers
from newsletters.models import Newsletter, Tags


class NewsletterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Newsletter
        fields = ('name','description','target','image','frequency', 'created_at', 'updated_at','author','tag','subscribed')

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = ('name','slug','created_at','updated_at')