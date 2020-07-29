from django.urls import path

from . import views


urlpatterns = [
    path('categories/', views.CategoriesView.as_view()),
    path('levels/', views.LevelView.as_view()),
    path('words/<int:pk>/', views.WordsView.as_view()),
    path('themes/', views.ThemesViewSet.as_view({'get': 'list'})),
    path('themes/<int:pk>/', views.ThemesViewSet.as_view({'get': 'retrieve'})),
]