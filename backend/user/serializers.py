from rest_framework import serializers
from user.models import User




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'email',
            'role',
            'f_name',
            'l_name',
            'is_active',
            'is_superuser',

        ]

  





   