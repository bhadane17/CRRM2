from django.urls import path, include
from . import views as auth_views
from screens import views as screen_views



urlpatterns = [
    path('', auth_views.login_user, name='login'),
    path('logout', auth_views.logout_user, name='logout'),
    path('introduction', screen_views.introduction, name='introduction'),
    path('score', screen_views.score, name='score'),
    path('first-screen', screen_views.first_screen, name='first-screen'),
    path('Customer_Type',screen_views.Customer_Type,name='Customer_Type'),
    path('weight_distribution', screen_views.weight_distribution, name='weight_distribution'),
    path('Product_Service', screen_views.Product_Service, name='Product_Service'),
    path('Juridictional_Risk', screen_views.Juridictional_Risk, name='Juridictional_Risk'),
    path('List_Matching', screen_views.List_Matching, name='List_Matching'),
    path('Profile_linkage', screen_views.Profile_linkage, name='Profile_linkage'),
    path('Transaction_Behavior', screen_views.Transaction_Behavior, name='Transaction_Behavior'),

]