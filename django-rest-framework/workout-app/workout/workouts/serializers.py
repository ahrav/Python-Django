from rest_framework import serializers
# from accounts.serializers import UserSerializer
from rest_framework.reverse import reverse as api_reverse

from .models import Workout

class WorkoutSerializer(serializers.ModelSerializer):
    user_id = serializers.HyperlinkedRelatedField(
        source='user',
        lookup_field='username',
        view_name='users:detail',
        read_only=True
    )
    user = serializers.SlugRelatedField(read_only=True, slug_field='username')
    # user = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Status
        fields = [
            'id',
            'user_id',
            'user',
            'name',
            'sets',
            'repetition',
            'load',
            'rate_of_perceived_exertion',
            'percent_of_one_rep_max',
            'date'
        ]
        read_only_fields = ['user']