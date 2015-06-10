from swampdragon.serializers.model_serializer import ModelSerializer


class RoomSerializer(ModelSerializer):
	class Meta:
		model = 'myapp.Room'
		publish_fields = ('title', )
		update_fields = ('title', )