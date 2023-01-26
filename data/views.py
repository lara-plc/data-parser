from django.shortcuts import render

from rest_framework.views import APIView, Request, Response, status
from .serializers import DataSerializer
from .parsing_logic import PlainTextParser
from .models import Data
from datetime import datetime


# Create your views here.
def index(request):
    return render(request, "data/index.html", {})


class DataView(APIView):
    parser_classes = [PlainTextParser]

    def post(self, request: Request, format=None) -> Response:

        archive_txt = request.data.decode("utf-8")

        list_data = archive_txt.split("\n")

        for file in list_data:
            date = datetime(
                int(file[1:5]),
                int(file[5:7]),
                int(file[7:9]),
                int(file[42:44]),
                int(file[44:46]),
                int(file[46:48]),
            )

            info_dict = {
                "type": file[0:1],
                "date_and_hour": date,
                "value": float(file[9:19]) / 100,
                "cpf": file[19:30],
                "credit_card": file[30:42],
                "owner": file[48:62],
                "company_name": file[62:80],
            }

            serializer = DataSerializer(data=info_dict)
            print(serializer)
            serializer.is_valid(raise_exception=True)
            print(serializer)
            serializer.save()

        return Response(status=status.HTTP_201_CREATED)

    def get(self, request: Request) -> Response:
        data = Data.objects.all()

        serializer = DataSerializer(data, many=True)

        return Response(serializer.data)