from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import exceptions
from authentication.Serializers.UserSerializer import AddUserSerializer, UserDetailSerializer, UserListSerializer

from authentication.models import User


class UserView(APIView):
    def get(self, request):
        try:
            query_set = User.objects.all()
            serializer = UserListSerializer(query_set, many=True)

            return Response(serializer.data, status=200)

        except Exception as e:
            return Response({"detail": str(e)}, status=422)

    def post(self, request):
        serializer = AddUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        else:
            return Response(serializer.errors, status=422)

    def put(self, request):
        try:
            obj_id = request.data["id"]
        except Exception as e:
            print(e)
            return Response({"detail": "ID not found in data!"}, status=422)

        user = User.objects.filter(id=obj_id).first()
        serializer = AddUserSerializer(user, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        else:
            return Response(serializer.errors, status=422)


class UserDetailView(APIView):
    def get(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
        except Exception as e:
            return Response({"detail": str(e)}, status=422)

        serializer = UserDetailSerializer(user)

        return Response(serializer.data)

    def delete(self, request, pk):
        try:
            User.objects.filter(id=pk).delete()
        except Exception as e:
            return Response({"detail": str(e)}, status=422)

        return Response({"detail": "Deleted User Successfully!"}, status=200)