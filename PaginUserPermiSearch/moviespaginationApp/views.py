# remember "request " contains everything from the webpage
from django.shortcuts import render
from django.views.generic.list import ListView  # this is for class based views
# Create your views here.
from .models import Movies
from django.core.paginator import Paginator

##1- class based view
#class MoviesClassView(ListView):  
 #   model = Movies
  #  template_name = 'moviespaginationApp/index.html'
   # context_object_name = 'item_lists'

##2 - function based view


# remember "request " contains everything from the webpage
def movie_list(request):
   movie_objects = Movies.objects.all()

   #getting the search key typed
   movie_name = request.GET.get('movie_name')

   if movie_name !='' and movie_name is not None:
      #movie_objects = movie_objects.filter(name=movie_name)  # this line search the exact word because of "name" parameter,which is one of the attributes of the model,  to optimize, let's use the below code
      movie_objects = movie_objects.filter(name__icontains=movie_name) # here we have double underscore "__" after name attribute
    
      
   #setting up pagination
   paginator = Paginator(movie_objects, 4)  # this means four objects per page
   page = request.GET.get('page') # getting the current page number, remenber request object contains everything in the webpage
   movie_objects = paginator.get_page(page)   # list of the movies of the current page
   
   context = {
       'movie_objects': movie_objects,
   }
   return render(request, 'moviespaginationApp/movie_list.html', context)