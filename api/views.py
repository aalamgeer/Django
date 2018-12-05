# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from api.serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .models import *
from rest_framework import status


@api_view(['POST'])
def add_country(request):
    country_serializer = CountrySerializer(data=request.data)
    if country_serializer.is_valid():
        country_serializer.save()
        return Response({'data':'You save successfully'}, status=status.HTTP_201_CREATED)
    else:
        error_details = []
        for key in country_serializer.errors.keys():
            error_details.append({'field': key, 'message': country_serializer.errors[key[0]]})

            data = {
                'Error':{
                    'status': 400,
                    'message': "Data submitted is not valid",
                    'error_details': error_details
                }
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def update_county(request, id):
    country_obj = Country.objects.get(id=id)

    if request.method == "GET":
        country_data = CountrySerializer(country_obj).data
        return Response({"data": country_data}, status=status.HTTP_200_OK)
    elif request.method == "DELETE":
        country_obj.delete()
        return Response({"data": "Country Deleted Successfully."}, status=status.HTTP_200_OK)
    else:
        country_serializer = CountrySerializer(country_obj, data=request.data)
        if country_serializer.is_valid():
            country_serializer.save()
            return Response({"data": "Country Updated successfully"}, status=status.HTTP_200_OK)
        else:
            error_details = []
            for key in country_serializer.errors.keys():
                error_details.append({"field": key, "message": country_serializer.errors[key][0]})
            data = {
                    "Error": {
                        "status": 400,
                        "message": "Your submitted data was not valid - please correct the below errors",
                        "error_details": error_details
                        }
                    }

            return Response(data, status=status.HTTP_400_BAD_REQUEST)


class employeeList(APIView):

    def get(self, request):
        employee1 = employee.objects.all()
        serializer = EmployeeSerializer(employee1, many=True)
        return Response(serializer.data)

    def post(self, request):
        pass
