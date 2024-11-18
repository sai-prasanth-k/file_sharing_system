# file_app/urls.py

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path
from .views import UserSignUpView, FileUploadView, FileDownloadView

urlpatterns = [
    path('signup/', UserSignUpView.as_view(), name='signup'),
    path('login/', TokenObtainPairView.as_view(), name='login'),  # Use JWT token view
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('upload-file/', FileUploadView.as_view(), name='upload-file'),
    path('download-file/<int:pk>/', FileDownloadView.as_view(), name='download-file'),
]