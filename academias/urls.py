from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from academias.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index.as_view(), name ='index'), 
]
