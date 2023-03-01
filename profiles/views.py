from django.http import JsonResponse
from django.shortcuts import render

from profiles.models import Profiles
from profiles.serializers import ProfileSerializer


# Create your views here.
def profile_list(request):
    if request.method == 'GET':
        my_profiles = Profiles.objects.all()
        my_ser = ProfileSerializer(my_profiles, many=True)
        return JsonResponse(my_ser.data, safe=False)