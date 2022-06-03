from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers
from .models import Phone


class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields = '__all__'


class PhoneAPIView(APIView):
    def get(self, request, id=None):
        if id:
            try:
                data = Phone.objects.get(pk=id)
                serializer = PhoneSerializer(data)
            except Exception as e:
                return Response({'Error': str(e), 'Code': 404})
        data = Phone.objects.all()
        serializer = PhoneSerializer(data, many=True)
        return Response({'Data': serializer.data, 'Code': 200})

    def post(self, request):
        data = request.data
        try:
            serializer = PhoneSerializer(data=data)
            if not serializer.is_valid():
                raise Exception
            serializer.save()
            return Response({'Message': 'User Added', 'Code': 200})
        except Exception as e:
            return Response({'Error': str(e), 'Code': 404})

    def put(self, request, id):
        try:
            phone_instance = Phone.objects.get(pk=id)
            if not phone_instance:
                raise Exception
            serializer = PhoneSerializer(instance=phone_instance, data=request.data, partial=True)
            if not serializer.is_valid():
                raise Exception
            serializer.save()
            return Response({'Message': 'Data Updated', 'Code': 200})
        except Exception as e:
            return Response({'Error': str(e), 'Code': 404})

    def delete(self, request, id):
        try:
            data = Phone.objects.get(pk=id)
            if not data:
                raise Exception
            data.delete()
            return Response({'Message': 'Data Deleted', 'Code': 200})
        except Exception as e:
            return Response({'Error': str(e), 'Code': 404})

