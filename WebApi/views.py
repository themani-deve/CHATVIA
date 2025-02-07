from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from WebApi.serializer import TextSerializer
from Main.views import process_pos_nev
from rest_framework import status


# Create your views here.


class PosNevApi(APIView):
    def post(self, request: Request):
        serializer = TextSerializer(data=request.data)
        if serializer.is_valid():
            text = serializer.validated_data['text']
            result = process_pos_nev(text=text)
            return Response({'result': result}, status=status.HTTP_200_OK)
        else:
            return Response(None, status=status.HTTP_400_BAD_REQUEST)
