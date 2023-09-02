from django.urls import path
from django.views.decorators.cache import cache_page

from dogs.apps import DogsConfig
from dogs.views import IndexView, CategoryListView, DogListView, DogCreateView, DogUpdateView, DogDeleteView

app_name = DogsConfig.name

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('categories/', cache_page(60)(CategoryListView.as_view()), name='categories'),
    path('<int:pk>/dogs/', DogListView.as_view(), name='category_dogs'),
    path('<int:pk>/create/', DogCreateView.as_view(), name='create_dog'),
    path('edit/<int:pk>', DogUpdateView.as_view(), name='edit_dog'),
    path('delete/<int:pk>/', DogDeleteView.as_view(), name='delete_dog')
]
