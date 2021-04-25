from django.contrib import admin
from .models import Category, Article

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)

""" Mostramos datos de solo lectura en la pagina de admin """
class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ('user','created_at','update_at')


    """ Asignamos el articulo al usuario registrado """
    def save_model(self, request, obj, form, change):
        if not obj.user_id:
            obj.user_id = request.user.id

        obj.save()

admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)