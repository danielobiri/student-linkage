import random
import os
from django.db import models
from PIL import Image
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from user.models import User, roles


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    new_filename = random.randint(1, 3910209312)
    name, ext = get_filename_ext(filename)
    final_filename = "{new_filename}{ext}".format(new_filename=new_filename, ext=ext)
    return "profile/{new_filename}/{final_filename}".format(
        new_filename=new_filename, final_filename=final_filename
    )


class Interest(models.Model):
    name = models.CharField(max_length=255, default="Interest")


class Publication(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    url = models.CharField(max_length=255, null=True, blank=True)


degree_statuses = (
    ("completed", "completed"),
    ("in_progress", "in_progress"),
)


degree_levels = (
    ("bachelor", "bachelor"),
    ("master", "master"),
    ("phd", "phd"),
    ("post_doc", "post_doc"),
    ("jd", "jd"),
)


class Course(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)


class Degree(models.Model):
    name = models.CharField(
        max_length=255, null=True, blank=True, choices=degree_levels
    )

    university = models.CharField(max_length=255, null=True, blank=True)

    status = models.CharField(
        max_length=255, choices=degree_statuses, default="in_progress"
    )
    courses = models.JSONField(
        null=True,
        blank=True,
    )  # min 5 max 7 not required recomended

    obtained_gpa = models.CharField(max_length=255, null=True, blank=True)

    total_gpa = models.CharField(max_length=255, null=True, blank=True)


titles = (
    ("Phd", "Phd"),
    ("Ms", "Ms"),
    ("Jd", "Jd"),
)

verification_methods = (
    ("email", "email"),
    ("id", "id"),
)


class University(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    student_id = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    is_verified = models.BooleanField(default=False)
    email = models.CharField(max_length=255, null=True, blank=True)
    verification_method = models.CharField(
        max_length=255, null=True, choices=verification_methods, blank=True
    )

    def __str__(self):
        return self.name


class Profile(models.Model):
    # student
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True, related_name="profile"
    )
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)

    university = models.OneToOneField(
        University,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="profile",
    )
    uni_data = models.JSONField(null=True, blank=True)
    image_small = ImageSpecField(
        source="image",
        processors=[ResizeToFill(100, 100)],
        format="webp",
        options={"quality": 100},
    )

    is_complete = models.BooleanField(default=False)

    image_small = ImageSpecField(
        source="image",
        processors=[ResizeToFill(300, 300)],
        format="webp",
        options={"quality": 100},
    )

    resume = models.FileField(
        upload_to=upload_image_path, null=True, blank=True
    )  # required

    google_scholar_page = models.CharField(max_length=255, null=True, blank=True)
    publications = models.ManyToManyField(
        Publication,
        blank=True,
    )  # min 0 max 4 required

    degrees = models.ManyToManyField(Degree, blank=True)
    degree_seeking = models.CharField(
        max_length=255, null=True, blank=True, choices=degree_levels
    )

    country = models.CharField(max_length=100, null=True, blank=True)

    address = models.CharField(max_length=100, null=True, blank=True)

    research_background = models.TextField(null=True, blank=True)  # max 50 words

    # professor -----------------------------------------------------

    title = models.CharField(max_length=100, null=True, blank=True)
    want_to_supervise = models.BooleanField(default=False)
    research_areas = models.JSONField(
        null=True,
        blank=True,
    )  # min 3 max 7 not required recomended

    interest_level = models.CharField(
        max_length=255, null=True, blank=True, choices=degree_levels
    )

    role = models.CharField(max_length=10, choices=roles, default="student")

    def __str__(self):
        return str(self.user)


class Job(models.Model):
    creator = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True, related_name="creator"
    )

    title = models.CharField(max_length=255, null=True, blank=True)
    education_level = models.CharField(
        max_length=255, null=True, blank=True, choices=degree_levels
    )

    interested = models.ManyToManyField(User, blank=True)  # user must be student


topics = (
    ("general", "general"),
    ("visa", "visa"),
    ("finance", "finance"),
    ("housing", "housing"),
)


class Like(models.Model):
    liked_by = models.ForeignKey(User, on_delete=models.CASCADE)


class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=255, null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(Like, blank=True)

    is_flagged = models.BooleanField(default=False)


class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=255, null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(Like, blank=True)
    topic = models.CharField(
        max_length=255,
        choices=topics,
    )
    is_flagged = models.BooleanField(default=False)

    answers = models.ManyToManyField(Answer, blank=True)
