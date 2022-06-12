from django.conf import settings
from django.core.mail import send_mail
from django.http import JsonResponse
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import NewUser
from .serializers import CustomUserSerializer


@api_view(["GET"])
def apiOverview(request):
    api_urls = {
        "List": "/user-list/",
        "Detail View": "/user-detail/<str:pk>/",
        "Create": "/user-create/",
        "Update": "/user-update/<str:pk>/",
        "Delete": "/user-delete/<str:pk>/",
    }

    return Response(api_urls)


@api_view(["GET"])
def userList(request):
    new_users = NewUser.objects.all().order_by("-code")
    serializer = CustomUserSerializer(new_users, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def userDetail(request, pk):
    new_users = NewUser.objects.get(code=pk)
    serializer = CustomUserSerializer(new_users, many=False)
    return Response(serializer.data)


@api_view(["POST"])
def userCreate(request):
    serializer = CustomUserSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    first_name = serializer.data.get("first_name")
    email_recipient = [serializer.data.get("email")]
    objetivo = serializer.data.get("objetivo")
    subject = "¡Rutina Seiken!"

    if objetivo == "perder_grasa":
        body = f"Hola {first_name}, tu objetivo es perder grasa"
        send_mail(subject, body, settings.EMAIL_HOST_USER, email_recipient)

    elif objetivo == "ganar_musculo":
        body = f"Hola {first_name}, tu objetivo es ganar musculo"
        send_mail(subject, body, settings.EMAIL_HOST_USER, email_recipient)

    elif objetivo == "ambos":
        body = f"Hola {first_name}, tu objetivo es perder grasa y ganar musculo"
        send_mail(subject, body, settings.EMAIL_HOST_USER, email_recipient)

    return Response(serializer.data)


@api_view(["POST"])
def userUpdate(request, pk):
    new_user = NewUser.objects.get(code=pk)
    serializer = CustomUserSerializer(instance=new_user, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(["DELETE"])
def userDelete(request, pk):
    new_user = NewUser.objects.get(code=pk)
    new_user.delete()

    return Response("User succsesfully deleted!")