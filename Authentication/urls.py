from django.urls import path, include
from . import views as auth_views
from screens import views as screen_views


urlpatterns = [
    path('', auth_views.login_user, name='login'),
    path('logout', auth_views.logout_user, name='logout'),
    path('introduction', screen_views.introduction, name='introduction'),
    path('score', screen_views.score, name='score'),
    path('first-screen', screen_views.first_screen, name='first-screen'),
    path('weight_distribution', screen_views.weight_distribution, name='weight_distribution'),
    path('weight_distribution_edit', screen_views.weight_distribution_edit, name='weight_distribution_edit'),
]