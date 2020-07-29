from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Categories, Level, Words, Themes


# Register your models here.


class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('name', 'preview')
    readonly_fields = ('preview',)

    def preview(self, obj):
        return mark_safe(f'<img src="{obj.get_url()}" width=50')


class ThemesAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'preview')
    readonly_fields = ('preview',)

    def preview(self, obj):
        print(obj.get_url())
        return mark_safe(f'<img src="{obj.get_url()}" width=50')


class WordsAdmin(admin.ModelAdmin):
    list_display = ('name', 'translation', 'player')

    readonly_fields = ('player',)

    def player(self, obj):
        template = f'<audio controls>' \
                   f'<source src={obj.get_url()} type="audio/mpeg">' \
                   f'<source src={obj.get_url()} type="audio/ogg">'\
                   f'</audio>'
        return mark_safe(template)


class LevelAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')


admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Level, LevelAdmin)
admin.site.register(Words, WordsAdmin)
admin.site.register(Themes, ThemesAdmin)