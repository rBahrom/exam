from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ServiceSerializers
from .models import Service


class ServiceAPIViewSet(APIView):
    pass


class ServiceDetail(APIView):
    def get(self, request):
        """

        :param request:
        :return:
        """
        query = Service.objects.all()
        search_data = request.query_params.get('search')
        if search_data is not None:
            query = query.filter(first_name__icontains=search_data)
        serializer = ServiceSerializers(query, many=True)
        return render(request, 'service.html', context=query)

    def post(self, request):
        """

        :param request:
        :return:
        """
        serializer = ServiceSerializers(data=request.data)
        if serializer.is_valid():
            service = serializer['service']
            check_service = Service.objects.get(id=service.id)
            if check_service:
                serializer.save()
                return Response(data=serializer.data)
            error = {
                'status': 400,
                'data': serializer.data,
                'message': "Error"
            }
            return Response(data=error, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id):
        service = Service.objects.get(id=id)
        serializer = ServiceSerializers(instance=service, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)

        error = {
            'status': 404,
            'message': 'Not Found'
        }
        return Response(data=error, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, id):
        """

        :param request:
        :param id:
        :return:
        """
        service = Service.objects.get(id=id)
        serializer = ServiceSerializers(instance=service, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)

        error = {
            'status': 404,
            'message': 'Not Found'
        }
        return Response(data=error, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, id):
        """

        :param request:
        :param id:
        :return:
        """
        service = Service.objects.get(id=id)
        service.delete()
        error = {
            'status': 404,
            'message': 'Music delete'
        }
        return Response(data=error, status=status.HTTP_204_NO_CONTENT)








