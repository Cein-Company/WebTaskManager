from rest_framework import serializers
from todo.models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'title', 'description', 'completed')
        #read_only_fields = ('id',)
        #extra_kwargs = {
        #    'completed': {'required': False}
        #}
        #fields = '__all__'
        #fields = ('id', 'title', 'description', 'completed')
        #read_only_fields = ('id',)
        #extra_kwargs = {
        #    'completed': {'required': False}
        #}
        #fields = '__all__'
        #fields = ('id', 'title', 'description', 'completed')
        #read_only_fields = ('id',)
        #extra_kwargs = {
        #    'completed': {'required': False}
        #}
        #fields = '__all__'
        #fields = ('id', 'title', 'description', 'completed')
        #read_only_fields = ('id',)
        #extra_kwargs = {
        #    'completed': {'required': False}
        #}
        #fields = '__all__'
        #fields = ('id', 'title', 'description', 'completed')
        #read_only_fields = ('id',)
        #extra_kwargs = {
        #    'completed': {'required': False}
        #}
        #fields = '__all__'
        #fields = ('id', 'title', 'description', 'completed')
        #read_only_fields = ('id',)
        #extra_kwargs = {
        #    'completed': {'required': False}
        #}
        #fields = '__all__'
        #fields = ('id', 'title', 'description', 'completed')
        #read_only_fields = ('id',)
        #extra_kwargs = {
        #    'completed': {'required': False}
        #}
        #fields = '__all__'
        #fields = ('id', 'title', 'description', 'completed')