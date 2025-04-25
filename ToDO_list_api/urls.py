from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todolist/', include('apps.ToDo_app.urls')),
    path('account/', include('apps.user_app.urls')),
]
