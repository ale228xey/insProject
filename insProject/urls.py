from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('photojournal.urls')),
    path('accounts/', include('accounts.urls'))
]

