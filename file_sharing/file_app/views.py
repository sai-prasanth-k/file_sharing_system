from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.core.mail import send_mail
from django.utils.crypto import get_random_string
from .models import User, File
from .serializers import UserSerializer, FileSerializer
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

class UserSignUpView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        verification_code = get_random_string(length=32)
        # Send verification email with verification_code
        send_mail(
            'Verify your email',
            f'Your verification code is {verification_code}',
            'from@example.com',
            [user.email],
            fail_silently=False,
        )

class LoginView(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'message': 'Login successful',
                'user': {
                    'id': user.id,
                    'username': user.username,
                    'email': user.email,
                    'is_ops_user': user.is_ops_user,
                }
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                'message': 'Invalid username or password'
            }, status=status.HTTP_401_UNAUTHORIZED)

class FileUploadView(generics.CreateAPIView):
    serializer_class = FileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        if not self.request.user.is_ops_user:
            return Response({"error": "Permission denied"}, status=status.HTTP_403_FORBIDDEN)
        serializer.save(user=self.request.user)

class FileDownloadView(generics.RetrieveAPIView):
    queryset = File.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        file = self.get_object()
        if file.user != request.user:
            return Response({"error": "Permission denied"}, status=status.HTTP_403_FORBIDDEN)
        # Generate a secure download link
        download_link = f"/download-file/{file.id}/"
        return Response({"download-link": download_link, "message": "success"})