from django.urls import path, include

from falcon.views import index

urlpatterns = [
    path('', index, name='index')
]