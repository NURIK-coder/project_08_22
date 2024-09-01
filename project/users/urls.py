from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView

from users.views import UserCreateApiView, GetCurrentUserAPIView, GetUserList, GetUserNotesApiView, ChangeUserRole

urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('register/', UserCreateApiView.as_view()),
    path('current_user/', GetCurrentUserAPIView.as_view()),
    path('list/', GetUserList.as_view()),
    path('<int:pk>/notes/', GetUserNotesApiView.as_view()),
    path('<int:pk>/change/role', ChangeUserRole.as_view())
]