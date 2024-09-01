from django.shortcuts import render
from rest_framework.generics import CreateAPIView, RetrieveAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from my_app.models import Note
from my_app.serializes import NoteSerializer
from users.models import User, Role
from users.serializers import UserCreateSerializer, UserSerializer


# Create your views here.


class UserCreateApiView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer

class GetCurrentUserAPIView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    lookup_field = None

class GetUserList(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GetUserNotesApiView(APIView):
    def get(self, request, pk):
        user = User.objects.get(id=pk)
        notes = Note.objects.filter(user_id=user)
        note_serialize = NoteSerializer(notes, many=True)
        return Response(note_serialize.data)

class ChangeUserRole(APIView):
    def post(self, request, pk):
        user = User.objects.get(id=pk)
        admin_role = Role.objects.get(name='admin')
        user.role = admin_role
        user.save()
        user_serialize = UserSerializer(user)
        return Response(user_serialize.data)
