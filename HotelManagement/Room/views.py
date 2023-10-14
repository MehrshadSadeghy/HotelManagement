from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response

from rest_framework.views import APIView

from .models import Room
from .serializer import RoomSerializer


class AllRoomView(APIView):
    def get(self, request):
        rooms = Room.objects.all()
        serializer = RoomSerializer(rooms, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RoomSearchView(APIView):
    def get(self, request, number):
        try:
            room = Room.objects.get(number=number)
            serializer = RoomSerializer(room)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Room.DoesNotExits:
            return Response(status=status.HTTP_404_NOT_FOUND)


class RoomFilterView(APIView):
    def get(self, request, filter):
        # filter for normal rooms
        if filter == "normal":
            rooms = Room.objects.filter(rank=1)
            serializer = RoomSerializer(rooms, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        # filter for vip rooms
        elif filter == "vip":
            rooms = Room.objects.filter(rank=2)
            serializer = RoomSerializer(rooms, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        # filter for empty rooms
        elif filter == "empty":
            rooms = Room.objects.filter(full=False)
            serializer = RoomSerializer(rooms, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

