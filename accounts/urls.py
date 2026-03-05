from django.urls import path
from accounts.views import author_list  

urlpatterns = [
    path('', author_list, name='author_list')
]