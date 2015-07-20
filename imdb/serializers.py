from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField
from imdb.models import UserProfile, Item


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('url', 'email', 'name', 'watch_list', 'pk')


class ItemSerializer(serializers.HyperlinkedModelSerializer):
    user_watch = PrimaryKeyRelatedField('user_watch', many=True)
    user_wish = PrimaryKeyRelatedField('user_wish', many=True)

    class Meta:
        model = Item
        fields = ('url', 'title', 'total_rate', 'user_watch', 'user_wish')
