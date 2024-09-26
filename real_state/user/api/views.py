from ..models import *
from rest_framework import status
from rest_framework.response import Response
from .serializers import *
from rest_framework.decorators import api_view

@api_view(['GET'])
def user_details(request,id):
    if request.method == 'GET':
        user = User.objects.get(pk=id)
        user_json = UserSerializer(user)
        return Response(data=user_json.data, status=200)
    return Response({"error message": "xxxxxx"})

@api_view(['GET'])
def all_user(request):
    if request.method == 'GET':
        user = User.objects.all()
        user_json = UserSerializer(user,many=True)
        return Response(data=user_json.data, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def add_user(request):
    if request.method == 'POST':
        user = UserSerializer(data=request.data)
        print('djkbkv')
        if User.objects.filter(**request.data).exists():
            print('djkbkv')
            raise serializers.ValidationError('This data already exists')
        if user.is_valid():
            user.save()
            return Response({"success message": "User Is Add"},status=status.HTTP_201_CREATED)
        else:
            print('ll')
            return Response(user.errors,status=status.HTTP_400_BAD_REQUEST)
    return Response({"error message": "xxxxxx"})

@api_view(['PUT'])
def update_user(request,id):
    user = User.objects.get(pk=id)
    user_json = UserSerializer(instance=user,data=request.data)
    if user_json.is_valid():
        user_json.save()
        return Response(user_json.data)
    else:
        return Response(user_json.errors,status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_user(request,id):
    user=User.objects.filter(id=id)
    if(len(user)>0):
        user.delete()
        return Response(data={'msg':'deleted'})
    return Response({'msg':'user not found'})




