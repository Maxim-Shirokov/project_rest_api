from rest_framework import serializers

from .models import Categories, Level, Words, Themes


class CategoriesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'


class LevelListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = '__all__'


class WordsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Words
        fields = '__all__'


class WordsThemesSerializer(WordsDetailSerializer):
    class Meta(WordsDetailSerializer.Meta):
        fields = ('id', 'name')


class ThemesListSerializer(serializers.ModelSerializer):
    class Meta:
        level = serializers.IntegerField
        model = Themes
        exclude = ('words',)


class ThemesDetailSerializer(serializers.ModelSerializer):
    words = WordsThemesSerializer(many=True)

    class Meta:
        model = Themes
        fields = '__all__'
