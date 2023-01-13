import csv

from rest_framework.response import Response
from rest_framework.views import APIView
from authentication.Serializers.RealEstateSerializer import AddRealEstateSerializer, RealEstateListSerializer, RealEstateSerializer

from authentication.models import RealEstate, User


class RealEstateView(APIView):
    def get(self, request):
        try:
            query_set = RealEstate.objects.all()
            serializer = RealEstateListSerializer(query_set, many=True)

            return Response(serializer.data, status=200)

        except Exception as e:
            return Response({"detail": str(e)}, status=422)

    def post(self, request):
        response_data = {}
        user_id = request.data.get("user", None)
        serializer = AddRealEstateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response_data1 = serializer.data
            user = User.objects.get(id=user_id)
            response_data["name"] = user.name
            response_data["email"] = user.email
            response_data["description"] = serializer.data.get("description")
            response_data["price"] = serializer.data.get("price")
            response_data["address"] = serializer.data.get("real_estate_address")
            filename = 'real_estate.csv'
            with open(filename, mode='a', newline='') as csv_file:
                fieldnames = list(response_data.keys())
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                if csv_file.tell() == 0:
                    writer.writeheader()
                writer.writerow(response_data)
            return Response(response_data, status=200)
        else:
            return Response(serializer.errors, status=422)

    def put(self, request):
        try:
            obj_id = request.data["id"]
        except Exception as e:
            print(e)
            return Response({"detail": "ID not found in data!"}, status=422)

        instance = RealEstate.objects.filter(id=obj_id).first()
        serializer = AddRealEstateSerializer(instance, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        else:
            return Response(serializer.errors, status=422)


class RealEstateDetailView(APIView):
    def get(self, request, pk):
        try:
            instance = RealEstate.objects.get(pk=pk)
        except Exception as e:
            return Response({"detail": str(e)}, status=422)

        serializer = RealEstateSerializer(instance)

        return Response(serializer.data)

    def delete(self, request, pk):
        try:
            RealEstate.objects.filter(id=pk).delete()
        except Exception as e:
            return Response({"detail": str(e)}, status=422)

        return Response({"detail": "Deleted Successfully!"}, status=200)


class UserRealEstateListingView(APIView):
    def get(self, request):
        try:
            user_id = request.GET.get("user_id", None)
            if user_id:
                query_set = RealEstate.objects.filter(user_id=user_id)
                serializer = RealEstateListSerializer(query_set, many=True)

                return Response(serializer.data, status=200)
            return Response([], status=200)

        except Exception as e:
            return Response({"detail": str(e)}, status=422)
