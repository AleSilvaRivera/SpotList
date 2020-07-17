from rest_framework import serializers
from api.models import User, UserProfile # importing our user and userprofile models

# Defining our serializers

#A serializers takes querysets or Django model instances as input and converts them to python data types
# so they can we convert them to JSON/XML


class UserProfileSerializer(serializers.ModelSerializer): # our UserProfileSerializer for UserProfile Model
    class Meta:
        model = UserProfile
        fields = ('phone',)  # the only extra field needed in the form that is not part of Django default user model

#DFR: Django Rest Framework
class UserSerializer(serializers.HyperlinkedModelSerializer): # built in classes of DRF
    #.HyperlinkedModelSerializer, serialices Django Models but instead of displaying the PK displays a hyperlink to
    #the model instance in the url field.
    profile = UserProfileSerializer(required=True)

    class Meta:
        model = User
        fields = ('url', 'email', 'first_name', 'last_name', 'password', 'profile')
        extra_kwargs = {'password': {'write_only': True}} # the password would be only visible when creating
        # an user object


# creating the user in the DB
    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        password = validated_data.pop('password')
        user = User(**validated_data) #validating the data entered by the user...
        user.set_password(password) # method to hash and store the password as hash instead of plain text
        user.save() # saving the user
        UserProfile.objects.create(user=user, **profile_data) # creating the user object
        return user
# updating an user object
    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile')
        profile = instance.profile

        instance.email = validated_data.get('email', instance.email)
        instance.save()

        profile.phone = profile_data.get('phone', profile.phone)
        profile.save()

        return instance