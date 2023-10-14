from django.db import models


class RoomRank(models.Model):
    rank = models.CharField(max_length=20, verbose_name="Room rank")

    def __str__(self):
        return self.rank


class Room(models.Model):
    number = models.IntegerField(verbose_name="Room number")
    rank = models.ForeignKey(RoomRank, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Room rank")
    full = models.BooleanField(default=False, verbose_name="Full or not")
    price = models.IntegerField(null=True, blank=True, verbose_name="Price")
    picture_1 = models.ImageField(upload_to="documents", null=True, blank=True, verbose_name="Picture num 1")
    picture_2 = models.ImageField(upload_to="documents", null=True, blank=True, verbose_name="Picture num 2")
    picture_3 = models.ImageField(upload_to="documents", null=True, blank=True, verbose_name="Picture num 3")
    options = models.TextField(verbose_name="Options", null=True, blank=True)
    score = models.IntegerField(blank=True, null=True)

    def __str__(self):
        number = str(self.number)
        return number


class Reservation(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, verbose_name="Room number")
    start = models.DateTimeField(verbose_name="Start reservation")
    end = models.DateTimeField(verbose_name="End reservation")

    def __str__(self):
        number = str(self.room)
        return number
