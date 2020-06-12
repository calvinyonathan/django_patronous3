from rest_framework import generics, mixins, permissions
from ..models import Reference
from .serializers import ReferenceSerializer
from django.contrib.auth import get_user_model
from .permissions import IsAuthorOrReadonly
from django.utils.text import slugify


class ReferenceListView(generics.ListCreateAPIView):
    queryset= Reference.objects.all()
    serializer_class = ReferenceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):   
        if serializer.is_valid():
            serializer.save(author=self.request.user)
    

# class ReferenceListView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Reference.objects.all()
#     serializer_class = ReferenceSerializer
#     permission_classes= [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadonly]
#     def perform_update(self,serializer):
#         if serializer.is_valid():
#             serializer.save(allow_unicode=True)


