from django.http import JsonResponse
# from django.shortcuts import render
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser
from rest_framework.views import APIView

from mix.custome_permission import IsOwner
from profiles.models import Profiles
from profiles.serializers import ProfileSerializer
from rest_framework import generics
from mix.custom_generic_views import PartialUpdateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.authentication import BaseAuthentication, SessionAuthentication, BasicAuthentication


# @csrf_exempt
# def profile_list(request):
#     if request.method == 'GET':
#         my_profiles = Profiles.objects.all()
#         my_ser = ProfileSerializer(my_profiles, many=True)
#         return JsonResponse(my_ser.data, safe=False)
#
#     if request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = ProfileSerializer(data = data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)

#
# class ProfileView(APIView):
#     def get(self, request):
#         my_profiles = Profiles.objects.all()
#         my_ser = ProfileSerializer(my_profiles, many=True)
#         return JsonResponse(my_ser.data, safe=False)
#
#     def post(self, request):
#         pass


# class ProfileView(generics.ListAPIView):
#     serializer_class = ProfileSerializer
#     queryset = Profiles.objects.all()


# class RetrieveProfileView(generics.RetrieveAPIView):
#     serializer_class = ProfileSerializer
#     queryset = Profiles.objects.all()
#     permission_classes = (IsAuthenticated,)


class RetrieveUpdateDestroyAPIViewProfile(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProfileSerializer
    queryset = Profiles.objects.all()
    permission_classes = (IsOwner,)


class ProfileView(generics.ListCreateAPIView):
    serializer_class = ProfileSerializer
    queryset = Profiles.objects.all()
    permission_classes = (AllowAny,)


'''class ProfileRetrieve(PartialUpdateAPIView):
    serializer_class = ProfileSerializer
    queryset = Profiles.objects.all()
    '''
