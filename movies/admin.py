from django.contrib import admin
import movies.models as movies_model


@admin.register(movies_model.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url')
    list_display_links = ('name',)


@admin.register(movies_model.Genre)
class Genre(admin.ModelAdmin):
    list_display = ('id', 'name', 'url')
    list_display_links = ('name',)

class ReviewInline(admin.TabularInline):
    model = movies_model.Reviews
    readonly_fields = ('name', 'email', 'parent')
    extra = 0


@admin.register(movies_model.Movie)
class MoviesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'url', 'year', 'draft',)
    list_display_links = ('title',)
    list_filter = ('category', 'year', 'draft')
    search_fields = ('title', 'category__name')
    inlines = [ReviewInline]
    save_on_top = True
    save_as = True
    fieldsets = (
        (None, {
            'fields': (('category', 'title', 'tagline',),)
        }),
        (None, {
            'fields': (('draft', 'url'),)
        }),
        (None, {
            'fields': (('poster',),)
        }),

        (None, {
            'fields': (('description',),)
        }),
        (None, {
            'fields': (('year', 'country', 'world_premiere'),)
        }),
        ('Дополнительно', {  # Название группы
            'classes': ('collapse',),  # Скрывает группу
            'fields': (('directors', 'actors', 'genres'),)
        }),
        (None, {
            'fields': (('budget', 'fess_in_usa', 'fess_in_world'),)
        }),
    )


@admin.register(movies_model.movie_shots)
class MovieShots(admin.ModelAdmin):
    list_display = ('id', 'title', 'movie',)
    list_display_links = ('title',)


@admin.register(movies_model.Rating)
class Rating(admin.ModelAdmin):
    list_display = ('star', 'movie')


@admin.register(movies_model.RatingStar)
class RatingStar(admin.ModelAdmin):
    list_display = ('id', 'value')


@admin.register(movies_model.Actor)
class Actor(admin.ModelAdmin):
    list_display = ('id', 'name', 'age')
    list_display_links = ('name',)


@admin.register(movies_model.Reviews)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'text', 'parent')  # Отображаемые поля в списке
    list_display_links = ('name',)  # Ссылка по полю
    list_filter = ('name', 'parent')  # Фильтр по полям
    search_fields = ('text',)  # Поиск по тексту
    readonly_fields = ('name', 'email')  # Запрет на редактирование через админку
