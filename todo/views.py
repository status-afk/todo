from rest_framework.generics import RetrieveAPIView
from .models import Todo
from rest_framework.viewsets import ModelViewSet
from .serializers import TodoSerializers




class TodoDetailApiView(ModelViewSet):
    serializer_class = TodoSerializers
    queryset = Todo.objects.all()
    lookup_field = 'id'



class BookViewSet(ModelViewSet):
    serializer_class = TodoSerializers
    queryset = Todo.objects.all()

