from django.urls import path
from .views import AdminOnlyView, StaffOnlyView, AuthenticatedView
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('admin-only/', AdminOnlyView.as_view()),
    path('staff-only/', StaffOnlyView.as_view()),
    path('auth-only/', AuthenticatedView.as_view()),
]