from django.urls import path

from wallpaperapi.views import ListRatings, ListCategories, ListWallpapers, WallpaperDetails

urlpatterns = [
    path('listratingss/', ListRatings.as_view(), name="ratings"),
    path('listcategorys/', ListCategories.as_view(), name="category"),
    # path('listwallpapers/', ListWallpapers.as_view(), name="wallpapers", kwargs={'pk': None}),
    path('listwallpapers/', ListWallpapers.as_view(),name="wallpapers",),
    path(r'listwallpapers/<int:pk>/', WallpaperDetails.as_view())
    # path('dummydata/', DummyDataView.as_view(), name="dummydata")
]
