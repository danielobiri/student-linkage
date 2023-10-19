import json
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse


# from .emailsend import email_send


from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from rest_framework import status
from user.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from core.serializers import ProfileSerializer

from core.models import Profile
from univ import validate_email
from core.models import University, Degree, Interest, Publication

import validators


def validate_url(url):
    output = validators.url(url)
    if output == True:
        return True
    return False


@api_view(["POST"])
def login_view(request):
    data = json.loads(request.body)
    print(data)
    email = data["email"]
    passwd = data["password"]
    obj = authenticate(email=email, password=passwd)
    if obj is not None:
        if obj.is_active:
            refresh = RefreshToken.for_user(obj)
            print(refresh, "tokens")
            return Response(
                {
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                    "role": obj.role,
                },
                status=status.HTTP_200_OK,
            )
        else:
            return Response({"msg": "inactive"}, status=status.HTTP_403_FORBIDDEN)
    else:
        return Response(
            {"msg": "authentication error"}, status=status.HTTP_401_UNAUTHORIZED
        )


@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def logout(request):
    logout(request)
    return Response({"status": "logged out"}, status=status.HTTP_200_OK)


@api_view(["POST"])
def signup_view(request):
    data = json.loads(request.body)
    print(data)
    email = data["email"]
    passwd = data["password"]
    fname = data["f_name"]
    lname = data["l_name"]
    role = data["role"]

    if not email or not passwd or not fname or not lname:
        return Response(
            {"msg": "Please fill all the fields"}, status=status.HTTP_400_BAD_REQUEST
        )

    if User.objects.filter(email=email).exists():
        return Response(
            {"msg": "A user with this email already exists"},
            status=status.HTTP_400_BAD_REQUEST,
        )
    u = None
    res = None
    # validate email if it is a university email
    res = validate_email(email)
    if not res["valid"]:
        return Response(
            {"msg": "Please enter a valid university email"},
            status=status.HTTP_400_BAD_REQUEST,
        )
    else:
        university = res["university"]
        u = University.objects.create(
            name=university["name"], email=email, verification_method="email"
        )

    user = User.objects.create(
        email=email,
        f_name=fname,
        l_name=lname,
        role=role,
    )

    user.set_password(passwd)

    # TODO: send email verification link

    p = Profile.objects.create(user=user, role=role, university=u)
    user.is_active = True
    user.save()
    return Response(
        {"msg": "User created successfully"}, status=status.HTTP_201_CREATED
    )


@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def get_user(request):
    try:
        user = request.user
        profile = Profile.objects.get_or_create(user=user)[0]

        serializer = ProfileSerializer(profile)

        return Response({"user": serializer.data}, status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return Response(
            {"msg": "Something went wrong"}, status=status.HTTP_400_BAD_REQUEST
        )


@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def basic_profile(request):
    file = request.FILES.getlist("profile_pic")
    f_name = request.POST.get("f_name")
    l_name = request.POST.get("l_name")
    country = request.POST.get("country")
    degree_seeking = request.POST.get("degree_seeking")
    title = request.POST.get("title")
    print(file, f_name, l_name, country, degree_seeking)

    try:
        user = request.user
        profile = Profile.objects.get_or_create(user=user)[0]

        user.f_name = f_name
        user.l_name = l_name
        user.save()
        if profile.role == "student":
            profile.country = country
            profile.degree_seeking = degree_seeking
        else:
            profile.title = title
            profile.interest_level = degree_seeking
        if file:
            profile.image = file[0]
        profile.save()

        serializer = ProfileSerializer(profile)

        return Response({"profile": serializer.data}, status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return Response(
            {"msg": "Something went wrong"}, status=status.HTTP_400_BAD_REQUEST
        )


@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def uni_verification(request):
    student_id = request.FILES.getlist("id")
    name = request.POST.get("name")
    verification_method = request.POST.get("verification_method")
    email = request.POST.get("email")
    print(student_id, name, verification_method, email)

    #     file = request.FILES.get('file')
    #     email = request.POST.get('email')
    #     password = request.POST.get('password')
    try:
        user = request.user
        profile = Profile.objects.get_or_create(user=user)[0]

        uni = profile.university

        if not uni:
            if verification_method == "email":
                if not email:
                    return Response(
                        {"msg": "Email is required"},
                        status=status.HTTP_400_BAD_REQUEST,
                    )

            else:
                if not student_id:
                    return Response(
                        {"msg": "Student id is required"},
                        status=status.HTTP_400_BAD_REQUEST,
                    )

            uni = University.objects.create(
                name=name,
                email=email,
                verification_method=verification_method,
                student_id=student_id[0] if student_id else None,
            )
            uni.email = email
            if email == user.email:
                uni.is_verified = True
            profile.university = uni
            profile.save()
        else:
            if uni.is_verified:
                return Response(
                    {"msg": "University already verified"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            uni.name = name

            uni.verification_method = verification_method
            if verification_method == "email":
                if not email and not uni.email:
                    return Response(
                        {"msg": "Email is required"},
                        status=status.HTTP_400_BAD_REQUEST,
                    )
                uni.email = email
                if email == user.email:
                    uni.is_verified = True
            else:
                if not student_id and not uni.student_id:
                    return Response(
                        {"msg": "Student id is required"},
                        status=status.HTTP_400_BAD_REQUEST,
                    )

                if uni.student_id:
                    pass
                else:
                    uni.student_id = student_id[0] if student_id else None

            uni.save()

        serializer = ProfileSerializer(profile)

        return Response({"profile": serializer.data}, status=status.HTTP_200_OK)
    except Exception as e:
        import traceback

        print(traceback.format_exc())
        print(e)
        return Response(
            {"msg": "Something went wrong"}, status=status.HTTP_400_BAD_REQUEST
        )


def validateDegree(deg):
    name = deg.get("name")
    university = deg.get("university")
    obtained_gpa = deg.get("obtained_gpa")
    total_gpa = deg.get("total_gpa")
    courses = deg.get("courses")
    if name and university and obtained_gpa and total_gpa:
        return True


@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def save_degree(request):
    data = json.loads(request.body)
    try:
        user = request.user
        profile = Profile.objects.get_or_create(user=user)[0]

        print(data)
        degs = profile.degrees.all()
        for deg in degs:
            deg.delete()
        if len(data) == 0:
            return Response(
                {"msg": "You must add one degree"}, status=status.HTTP_400_BAD_REQUEST
            )
        for deg in data:
            if validateDegree(deg):
                degree = Degree.objects.create(
                    name=deg.get("name"),
                    university=deg.get("university"),
                    status=deg.get("status"),
                    obtained_gpa=deg.get("obtained_gpa"),
                    total_gpa=deg.get("total_gpa"),
                    courses=deg.get("courses"),
                )
                profile.degrees.add(degree)
            else:
                return Response(
                    {"msg": "Invalid degree data"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

        serializer = ProfileSerializer(profile)

        return Response({"profile": serializer.data}, status=status.HTTP_200_OK)
    except Exception as e:
        import traceback

        print(traceback.format_exc())
        print(e)
        return Response(
            {"msg": "Something went wrong"}, status=status.HTTP_400_BAD_REQUEST
        )


@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def save_research(request):
    resume = request.FILES.getlist("resume")
    google_scholar = request.POST.get("google_scholar")
    interests = request.POST.get("interests")
    research_background = request.POST.get("research_background")

    print(
        resume,
        google_scholar,
        interests,
        research_background,
    )
    try:
        if validate_url(google_scholar) == False:
            return Response(
                {"msg": "Invalid google scholar url"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        user = request.user
        profile = Profile.objects.get_or_create(user=user)[0]
        if resume:
            profile.resume = resume[0]
        profile.google_scholar_page = google_scholar
        profile.research_background = research_background
        ni = []
        interests = json.loads(interests)

        profile.research_areas = interests

        profile.save()
        serializer = ProfileSerializer(profile)
        print(serializer.data)

        return Response({"profile": serializer.data}, status=status.HTTP_200_OK)
    except Exception as e:
        import traceback

        print(traceback.format_exc())
        print(e)
        return Response(
            {"msg": "Something went wrong"}, status=status.HTTP_400_BAD_REQUEST
        )


def validatePublication(deg):
    name = deg.get("name")
    url = deg.get("url")

    if name and url:
        return True
    else:
        return False


@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def save_publication(request):
    data = json.loads(request.body)
    try:
        user = request.user
        profile = Profile.objects.get_or_create(user=user)[0]

        print(data)
        degs = profile.publications.all()
        for deg in degs:
            deg.delete()
        for deg in data:
            if validatePublication(deg):
                print(validate_url(deg.get("url")))
                if validate_url(deg.get("url")) == False:
                    return Response(
                        {"msg": "Invalid url"},
                        status=status.HTTP_400_BAD_REQUEST,
                    )
                pub = Publication.objects.create(
                    name=deg.get("name"),
                    url=deg.get("url"),
                )
                profile.publications.add(pub)
            else:
                return Response(
                    {"msg": "Invalid publication data"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
        profile.save()

        serializer = ProfileSerializer(profile)

        return Response({"profile": serializer.data}, status=status.HTTP_200_OK)
    except Exception as e:
        import traceback

        print(traceback.format_exc())
        print(e)
        return Response(
            {"msg": "Something went wrong"}, status=status.HTTP_400_BAD_REQUEST
        )


def check_if_complete(profile):
    if profile.role == "student":
        if profile.university is None:
            return {
                "msg": "Please fill in your university details",
                "status": False,
                "signup": "university",
            }

        if profile.degrees.count() == 0:
            return {
                "msg": "Please fill in your degree details",
                "status": False,
                "signup": "degree",
            }

        if (
            profile.resume == None
            or profile.research_background == None
            or profile.google_scholar_page == None
        ):
            return {
                "msg": "Please upload your resume",
                "status": False,
                "signup": "research",
            }

        if (
            profile.user.f_name == None
            or profile.user.l_name == None
            or profile.country == None
        ):
            return {
                "msg": "Please fill in your details",
                "status": False,
                "signup": "basic",
            }
    else:
        if (
            profile.user.f_name == None
            or profile.user.l_name == None
            or profile.interest_level == None
        ):
            return {
                "msg": "Please fill in your details",
                "status": False,
                "signup": "basic",
            }

        if profile.research_background == None or profile.google_scholar_page == None:
            return {
                "msg": "Please fill in your details",
                "status": False,
                "signup": "research",
            }

    return {
        "msg": "Profile is complete",
        "status": True,
        "signup": "complete",
    }


@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def mark_complete(request):
    data = json.loads(request.body)
    try:
        user = request.user
        profile = Profile.objects.get_or_create(user=user)[0]

        print(data)

        res = check_if_complete(profile)
        if res["status"] == True:
            profile.is_complete = True
            profile.save()
        else:
            return Response(res, status=status.HTTP_400_BAD_REQUEST)
        serializer = ProfileSerializer(profile)

        return Response({"profile": serializer.data}, status=status.HTTP_200_OK)
    except Exception as e:
        import traceback

        print(traceback.format_exc())
        print(e)
        return Response(
            {"msg": "Something went wrong"}, status=status.HTTP_400_BAD_REQUEST
        )
