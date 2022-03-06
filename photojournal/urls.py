from django.urls import path
from photojournal.views import MainPageView

urlpatterns = [
    path('', MainPageView.as_view())
]