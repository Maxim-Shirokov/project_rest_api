from django.db.models import Prefetch
from rest_framework import generics, viewsets

from .models import Categories, Level, Words, Themes
from .serializers import (
    CategoriesListSerializer,
    LevelListSerializer,
    WordsDetailSerializer,
    ThemesListSerializer,
    ThemesDetailSerializer
)

from django.db import connection


# Create your views here.
class CategoriesView(generics.ListAPIView):
    serializer_class = CategoriesListSerializer
    queryset = Categories.objects.all()


class LevelView(generics.ListAPIView):
    serializer_class = LevelListSerializer
    queryset = Level.objects.all()


class WordsView(generics.RetrieveAPIView):
    queryset = Words.objects.all()
    serializer_class = WordsDetailSerializer


class ThemesViewSet(viewsets.ReadOnlyModelViewSet):
    def get_queryset(self):
        queryset = Themes.objects.all()
        category = self.request.query_params.get('category')
        level = self.request.query_params.get('level')

        if category:
            queryset = queryset.filter(category_id=category)

        if level:
            queryset = queryset.filter(level=level).prefetch_related(
                Prefetch('level', queryset=Level.objects.filter(id=level)))

        return queryset

    def get_serializer_class(self):
        if self.action == 'list':
            return ThemesListSerializer
        if self.action == 'retrieve':
            return ThemesDetailSerializer
