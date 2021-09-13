from account.serializers import UserSerializer
from django.shortcuts import get_object_or_404, render
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User

class ProfileView(RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_object(self):
        querset = self.get_queryset()
        obj = get_object_or_404(querset, id = self.request.user.id)
        return obj  

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)