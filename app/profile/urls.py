from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profile import views

router = DefaultRouter()

router.register('profiles', views.ProfileViewSet)
router.register('matches', views.ProfileMatchesViewSet, basename='profile-matches')
router.register('profile-availability', views.ProfileAvailabilityViewSet)
router.register('nearby-profiles', views.NearbyProfilesViewSet, basename='nearby-profiles')


urlpatterns = [
    path('login/', views.UserLoginApiView.as_view()),
    path('register/', views.UserRegisterApiView.as_view()),
    path('ai-based-match/', views.AIBaseSuggestionView.as_view()),
    path('', include(router.urls)),
]