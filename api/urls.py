from django.urls import path
from .views import ListSongsView, DummyDataView

urlpatterns = [
    path('songs/', ListSongsView.as_view(), name="songs-all"),
    path('dummydata/', DummyDataView.as_view(), name="dummydata")
]
