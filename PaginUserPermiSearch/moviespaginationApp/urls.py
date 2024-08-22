from django.urls import path
from . import views

app_name = 'moviespaginationApp'

urlpatterns = [
        #path('', views.MoviesClassView.as_view(),  name='index'),
    path('', views.movie_list,  name='movie_list'),

]
