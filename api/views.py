from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from api.models import User
from api.serializers import UserSerializer
# Also add these imports
from api.permissions import IsLoggedInUserOrAdmin, IsAdminUser

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all() # list of the user objects
    serializer_class = UserSerializer # serializer class to be used for the model instances

    # permissions, who can delete or update users....
    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [AllowAny]  # anyone can create an user or register himself
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsLoggedInUserOrAdmin]
        elif self.action == 'list' or self.action == 'destroy':
            permission_classes = [IsAdminUser] # it has to be an user....
        return [permission() for permission in permission_classes]