__author__ = 'jonathan'

from django.contrib.auth.models import User
from rest_framework import serializers
from mordor.models import Person, Snippet


class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(
        many=True,
        view_name='mordor:snippet_detail',
        read_only=True
    )

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'snippets', 'is_staff')


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('name', 'identifier', 'id')


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(
        view_name='mordor:snippet_highlight',
        format='html'
    )

    class Meta:
        model = Snippet
        fields = (
            'id',
            'created',
            'title',
            'code',
            'linenos',
            'language',
            'style',
            'owner',
            'highlighted',
            'highlight',
        )



