from django.contrib import admin
#import class yang dibutuhkan untuk memodifikasi form pada User ADmin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

# import helper timezone untuk mengeset waktu published_at
from django.utils import timezone


#import class model Category dan News
from .models import Category, News


# Register your models here.

#Menambahkan Modul Category ke Admin

class CategoryAdmin(admin.ModelAdmin):
    #Menampilkan kolom 'name' dan 'created_at' pada halaman Category list di Admin
    list_display = ('name', 'created_at')
    #Menambahkan fitur pencarian berdasarkan kolom 'name'
    search_fields = ['name']

#Mendaftarkan CategoryAdmin

admin.site.register(Category, CategoryAdmin)

#Membuat Custom Form untuk Form Add User

class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','first_name','last_name',)

#Membuat Custom Form untuk Form Update User

class UserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username','first_name','last_name',)

# Mengeset Custom User Form ke modul User Admin
class UserAdmin(UserAdmin):
    add_form = UserCreateForm
    form = UserUpdateForm
    prepopulated_fields = {'username':('first_name','last_name',)}

    add_fieldsets = (
        (None, {
            'classes':('wide',),
            'fields':('first_name', 'last_name','email', 'username','password1','password2',),

        }),
    )

    fieldsets = (
        (None, {
            'classes':('wide',),
            'fields':('first_name','last_name','email','username'),
        }),
        
    )

# Mendaftarkan ulang User Admin

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

# Menambahkan modul News ke Admin

class NewsAdmin(admin.ModelAdmin):
    #Menampilkan kolom 'title', 'status','user' dan 'created_at' pada halam News list di Admin

    list_display = ('title','status','user','created_at')

    #Menampilkan kolom

    fields = ('title','content','excerpt','cover','status','category')

    # Menambahkan fitur pencariaan berdasarkan kolom 'title'

    search_fields = ['title']
    # Menambahkan fitur filter data berdasarkan kolom 'status'
    list_filter = ('status',)

    #override method save_model untuk menyimpan data user dan published_at secara otomatis

    def save_model(self, request, obj, form, change):
        # menyimpan kolom 'user' berdasarkan user yang login
        if not obj.user_id:
            obj.user = request.user

        if form.cleaned_data.get('status') == 1:
            #mengeset kolom 'published_at' dengan nilai null jika status bernilai 1 (draft)
            obj.published_at = None

        else:
            #mengeset kolom 'published_at' dengan tanggal & waktu sekarang jika status bernilai 2 (published)
            obj.published_at = timezone.now()
        
        obj.save()

# Mendaftarkan NewsAdmin
admin.site.register(News, NewsAdmin)
    