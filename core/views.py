from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework import authentication
from .serializers import ListSerializer,ItemSerializer
from .models import List,Item


class ListViewSet(viewsets.ModelViewSet):
    #queryset = List.objects.all()
    serializer_class = ListSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication,
                              authentication.SessionAuthentication]
    '''filtrando listas por user/ ele substitui o atributo queryset'''
    def get_queryset(self):
        user = self.request.user
        ''' owner é chave estrangeira para user.name'''
        return List.objects.filter(owner=user)




class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication,
                              authentication.SessionAuthentication]