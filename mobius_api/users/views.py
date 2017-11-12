from django.contrib.auth import authenticate, login
from rest_framework import mixins, viewsets
from rest_framework.permissions import AllowAny
from django.views.generic.edit import FormView


from .models import User
from .permissions import IsUserOrReadOnly
from .serializers import CreateUserSerializer, UserSerializer
from .forms import CustomUserCreationForm


class UserViewSet(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    """
    Creates, Updates, and retrives User accounts
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsUserOrReadOnly,)

    def create(self, request, *args, **kwargs):
        self.serializer_class = CreateUserSerializer
        self.permission_classes = (AllowAny,)
        return super(UserViewSet, self).create(request, *args, **kwargs)


class RegistrationView(FormView):
    template_name = 'registration/login.html'
    form_class = CustomUserCreationForm
