from django.urls import path
#from . import views
from .views import (
    business_user_list, register, business_user_delete
)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('business-users/', business_user_list, name='business_user-list'),  # Obsługa GET i POST dla listy użytkowników
    path('business-users/<int:pk>/', business_user_delete, name='business_user-delete'),  # Obsługa DELETE dla użytkownika
    path('register/', register, name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh')
]

