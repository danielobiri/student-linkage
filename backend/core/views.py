import json
from core.serializers import *

from django.shortcuts import get_object_or_404

# from django.contrib.auth import authenticate, login, logout
# from django.utils import timezone
# from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.db import IntegrityError

# from accounts.models import User
from rest_framework.pagination import PageNumberPagination
from core.models import Job, Question, Answer, Like
from rest_framework import generics

# @api_view(["POST"])
# @permission_classes((IsAuthenticated, ))
# def create_api(request):
#     f = request.FILES['file']
#     n = request.POST.get('name')
#     ad = request.POST.get('address')
#     try:
#         p = Model.objects.create(name=n, location=ad, logo=f)
#     except IntegrityError:
#         return Response({"message": "Model already exists"}, status=status.HTTP_409_CONFLICT)
#     except Exception as e:
#         print(e)
#         return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)

#     return Response({'message': 'success'}, status = status.HTTP_200_OK)


# @api_view(["POST"])
# @permission_classes((IsAuthenticated, ))
# def profile_api(request):
#     return Response({"fname" : request.user.fname, "lname" : request.user.lname, "credit":request.user.credit, "is_investor":(request.user.is_prop_dealer == False)})


# @api_view(["POST"])
# @permission_classes((IsAuthenticated, ))
# def api_with_pages(request):


#     paginator = PageNumberPagination()
#     paginator.page_size = 20
#     ideas = Project.objects.all().order_by("-created_at")
#     result_page = paginator.paginate_queryset(ideas, request)
#     serializer = ProjectSerializer(result_page, many=True)
#     return paginator.get_paginated_response(serializer.data)


# @api_view(["POST"])
# @permission_classes((IsAuthenticated, ))
# def api_with_parameter(request, id):
#     try:
#         p = Project.objects.get(id=id)
#         serializer = ProjectSerializer(p)
#         return Response({"message": "success", "project": serializer.data}, status=status.HTTP_200_OK)
#     except Project.DoesNotExist:
#         return Response({"message": "Project does not exist"}, status=status.HTTP_404_NOT_FOUND)


@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def create_job(request):
    data = json.loads(request.body)

    try:
        # do something with data

        if request.user.role == "professor":
            title = data.get("title")
            education_level = data.get("education_level")
            Job.objects.create(
                title=title,
                education_level=education_level,
                creator=request.user,
            )

            return Response({"message": "success"}, status=status.HTTP_201_CREATED)

        else:
            return Response(
                {"message": "You are not a professor"},
                status=status.HTTP_400_BAD_REQUEST,
            )

    except Exception as e:
        print(e)
        return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def job_list(request):
    data = json.loads(request.body)

    try:
        if request.user.role == "student":
            jobs = Job.objects.all()

            serializer = JobSerializer(jobs, many=True)

            return Response(
                {"message": "success", "jobs": serializer.data},
                status=status.HTTP_200_OK,
            )

        else:
            return Response(
                {"message": "You are not a professor"},
                status=status.HTTP_400_BAD_REQUEST,
            )

    except Exception as e:
        print(e)
        return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def question_create(request):
    data = json.loads(request.body)

    try:
        print(data)

        q = Question.objects.create(
            title=data.get("title"),
            username=data.get("username"),
            message=data.get("message"),
            topic=data.get("topic"),
            user=request.user,
        )

        serializer = QuestionSerializer(q)

        return Response(
            {"message": "created", "question": serializer.data},
            status=status.HTTP_201_CREATED,
        )

    except Exception as e:
        print(e)
        return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def answer_create(request, id):
    data = json.loads(request.body)

    try:
        print(data)

        q = get_object_or_404(Question, id=id)
        a = Answer.objects.create(
            message=data.get("message"),
            user=request.user,
        )
        q.answers.add(a)
        q.save()

        serializer = AnswerSerializer(
            q.answers.all().order_by("-created_at"), many=True
        )

        return Response(
            {
                "message": "created",
                "answers": serializer.data,
                "question": QuestionSerializer(q).data,
            },
            status=status.HTTP_201_CREATED,
        )

    except Exception as e:
        print(e)
        return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
# @permission_classes((IsAuthenticated,))
def answers(request, id):
    data = json.loads(request.body)

    try:
        print(data)

        q = get_object_or_404(Question, id=id)

        serializer = AnswerSerializer(q.answers, many=True)

        return Response(
            {
                "message": "created",
                "answers": serializer.data,
                "question": QuestionSerializer(q).data,
            },
            status=status.HTTP_200_OK,
        )

    except Exception as e:
        print(e)
        return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def like(request, w, id):
    try:
        if not w in ["q", "w"]:
            return Response(
                {"message": "not valid url"}, status=status.HTTP_400_BAD_REQUEST
            )
        if w == "q":
            o = get_object_or_404(Question, id=id)
        else:
            o = get_object_or_404(Answer, id=id)

        if o.likes.filter(liked_by=request.user).exists():
            print("already liked")
        else:
            l = Like.objects.get_or_create(liked_by=request.user)[0]
            o.likes.add(l)
            o.save()
            print("new like added")

        return Response(
            {
                "message": "Liked",
            },
            status=status.HTTP_200_OK,
        )

    except Exception as e:
        print(e)
        return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
# @permission_classes((IsAuthenticated,))
def questions_list(request):
    data = json.loads(request.body)

    try:
        print(data)

        q = Question.objects.filter(
            topic=data.get("topic"),
        ).order_by("-created_at")

        serializer = QuestionSerializer(q, many=True)

        return Response(
            {"message": "created", "questions": serializer.data},
            status=status.HTTP_200_OK,
        )

    except Exception as e:
        print(e)
        return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)


# @api_view(["POST"])
# @permission_classes((IsAuthenticated, ))
# def api_recieves_form_data(request, id):
#     files = request.FILES.getlist('files')
#     file = request.FILES.get('file')
#     email = request.POST.get('email')
#     password = request.POST.get('password')
#     try:
#         #do something with data
#         return Response({"message": "success"}, status=status.HTTP_200_OK)

#     except Exception as e:
#         print(e)
#         return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)
