from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('iscae_app.urls')),
    path('admin/', admin.site.urls),

    # path('say_hello/', say_hello_json),
    # path('html_page/',html_page),
]
