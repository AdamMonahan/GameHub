from django.urls import path
from . import views

urlpatterns = [
    #localhost:8000/discuss
    path('', views.discuss),
    path('<int:post_id>/delete', views.delete),
    path('create', views.create),
]