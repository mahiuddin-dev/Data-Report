from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Category, SubCategory, Person

from .widgets import SubCategorySelect

# Register your models here.


class AdminCategory(admin.ModelAdmin):
    list_display = ["name"]
    list_per_page = 15
    search_fields =["name"]

class AdminSubCategory(admin.ModelAdmin):
    list_display = ['name']
    list_per_page = 15
    search_fields = ["name"]

class AdminPerson(admin.ModelAdmin):
    list_display = ["name","category","sub_category", "phone_number", "address"]

    list_filter = ["category","sub_category","upozila","union", "village"]
    list_per_page = 15
    list_select_related = True
    search_fields = ["name__icontains", "phone_number__icontains", "address__icontains"]
    formfield_overrides = {
        SubCategory : {'widget' : SubCategorySelect}
    }


admin.site.register(Category, AdminCategory)
admin.site.register(SubCategory, AdminSubCategory)
admin.site.register(Person, AdminPerson)