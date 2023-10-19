from django.contrib.auth import models
from django.db.models import fields
from rest_framework import serializers
from user.models import User
from core.models import (
    Course,
    Profile,
    Degree,
    Interest,
    Publication,
    Job,
    University,
    Question,
    Answer,
)
from user.serializers import UserSerializer


class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = "__all__"


class InterestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interest
        fields = "__all__"


class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class DegreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Degree
        fields = "__all__"


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    university = UniversitySerializer()
    # research_areas = InterestSerializer(many=True)
    publications = PublicationSerializer(many=True)
    degrees = DegreeSerializer(many=True)

    class Meta:
        model = Profile
        fields = "__all__"


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = "__all__"


class QuestionSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    likes = serializers.SerializerMethodField()

    class Meta:
        model = Question

        # fields = "__all__"
        exclude = ["likes"]

    def get_username(self, obj):
        return obj.user.f_name

    def get_likes(self, obj):
        return obj.likes.all().count()


class AnswerSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()

    class Meta:
        model = Answer

        # fields = "__all__"
        exclude = ["likes"]

    def get_username(self, obj):
        return obj.user.f_name

    def get_likes(self, obj):
        return obj.likes.all().count()


# class ModelSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = SomeModel
#         fields = '__all__'
#         #or
#         # exclude = ['id']
#         read_only_fields = ['id']


# class CustomSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=100)
#     logo = serializers.ImageField()
#     email = serializers.EmailField()
#     def create(self, validated_data):
#         pass
#     def update(self, instance, validated_data):
#         pass


# class SerializerWithMethodFields(serializers.ModelSerializer):
#     name = serializers.SerializerMethodField(read_only=True)

#     class Meta:
#         model = Modal
#         fields = ['id',  'name', 'created_at',  ]

#     def get_name(self, obj):
#         name = f"{obj.investor.fname} {obj.investor.lname}"
#         return name
