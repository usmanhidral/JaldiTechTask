from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt


# @csrf_exempt
# class LoginView(APIView):
#
#     @action(methods=['post'], detail=False)
#     def login(self, request):
#         username = request.data.get('username_or_email')
#         password = request.data.get('password')
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return Response({"detail": "User Log in Successfully!"}, status=status.HTTP_200_OK)
#         else:
#             return Response(status=status.HTTP_401_UNAUTHORIZED)
#
#
# @csrf_exempt
# class LogoutView(APIView):
#
#     @action(methods=['post'], detail=False)
#     def logout(self, request):
#         logout(request)
#         return Response(status=status.HTTP_204_NO_CONTENT)
