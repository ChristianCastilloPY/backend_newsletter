from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from newsletters.models import Newsletter, Tags
# from newsletters.permissions import CustomNewslettersPermissions
from newsletters.serializers import NewsletterSerializer, TagSerializer

class NewsletterViewSets(viewsets.ModelViewSet):
    """retrieve:
        Regresa un boletin
    list:
        Regresa la lista de boletines
    update:
        Actualiza un boletin
    partial_update:
        Actualiza un campo de un boletin
    delete:
        Elimina un boletin
    """
    queryset = Newsletter.objects.all()
    serializer_class = NewsletterSerializer
    # permission_classes = CustomNewslettersPermissions

    # def get_queryset(self):
    #     if self.request.query_params:
    #         tag = self.request.query_params.get('tag', None)
    #         if tag:
    #             return Newsletter.objects.filter(tag=tag)
    #         return Newsletter.objects.all()

    def get_permissions(self):
        if self.action in ['retrieve','list', 'tags']:
            self.permission_classes = [AllowAny]
        return [permission() for permission in self.permission_classes]

    #     if self.action == 'create':
    #         self.permission_classes = [IsAdminUser]
    #     return [permisiion() for permission in self.permission_classes]

    #/newsletters/1/tag
    @action(detail=True, methods=['GET'])
    def tags(self, request, pk=None):
        newsletter = self.get_objects()
        tags = newsletter.tags.all()
        page = self.paginate_queryset(tags)

        if page:
            serialized = self.get_serializer(page, many=True)
            return self.get_paginated_response(serialized.data)

        serialized = TagSerializer(tags, many=True)
        return Response(status= status.HTTP_200_OK, data= serialized.data)



class TagsViewSets(viewsets.ModelViewSet):
    queryset = Tags.objects.all()
    serializer_class = TagSerializer

    def get_permissions(self):
        if self.action in ['retrieve','list', 'tags']:
            self.permission_classes = [AllowAny]
        return [permission() for permission in self.permission_classes]
