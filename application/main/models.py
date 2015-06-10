from django.db import models
from swampdragon.models import SelfPublishModel
from .serializers import FooSerializer


class Room(SelfPublishModel, models.Model):
	serializer_class = RoomSerializer
	title = models.CharField(max_length=100)