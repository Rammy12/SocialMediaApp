from rest_framework import serializers
from app.models import User,UserFollow
from django.contrib.auth.hashers import make_password
class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = '__all__'
        extra_kwargs={
            'password':{'write_only':True}
        }
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        user = User.objects.create(**validated_data)
        return user
    
    def validate(self,validated_data):
        return validated_data
    


class UserLoginSerializer(serializers.ModelSerializer):
    email=serializers.EmailField(max_length=255)
    class Meta:
        model=User
        fields=['email','password']


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','first_name','last_name','username','email','bio']


class UserChangePasswordSerializer(serializers.ModelSerializer):
    password=serializers.CharField(max_length=255,write_only=True)
    password2=serializers.CharField(max_length=255,write_only=True)
    class Meta:
        model=User
        fields=['password','password2']

    def validate(self,validated_data):
        password=validated_data['password']
        password2=validated_data['password2']
        user=self.context['user']
        if password!=password2:
            raise serializers.ValidationError('Password and Conform Password does not match')
        user.set_password(password)
        user.save()
        return validated_data
    


class UserFollowSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserFollow
        fields = '__all__'
