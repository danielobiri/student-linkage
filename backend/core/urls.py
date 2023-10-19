from django.urls import path
from .views import *

urlpatterns = [
    # path('model/get/<str:id>/', get_model),
    path("job/create/", create_job),
    path("job/list/", job_list),
    path("community/create/", question_create),
    path("community/get/", questions_list),
    path("community/q/<int:id>/answer/", answer_create),
    path("community/q/<int:id>/", answers),
    path("like/<str:w>/<int:id>/", like),
]
