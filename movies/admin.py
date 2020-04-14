from django.contrib import admin
import movies.models as movies_model

# Register your models here.
admin.site.register(movies_model.Category)

admin.site.register(movies_model.Genre)
admin.site.register(movies_model.Movie)
admin.site.register(movies_model.movie_shots)
admin.site.register(movies_model.Rating)
admin.site.register(movies_model.RatingStar)

admin.site.register(movies_model.Actor)
admin.site.register(movies_model.Reviews)
