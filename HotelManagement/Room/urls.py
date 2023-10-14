from django.contrib import admin
from django.urls import path, include
from .views import AllRoomView, RoomSearchView, RoomFilterView

urlpatterns = [
    path("all/", AllRoomView.as_view()),
    path("search/<str:number>/", RoomSearchView.as_view()),
    path("filter/<str:filter>/", RoomFilterView.as_view()),
]
