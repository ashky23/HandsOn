import json
from pydantic.utils import deep_update

from django.shortcuts import render
from django_filters import rest_framework as filters
from rest_framework import viewsets, pagination, status
from rest_framework.response import Response

from pikachu.dto.pikachu import PikachuObject
from pikachu.services.pikachu import PikachuService
from pikachu.models import Pikachu


class PikachuViewSet(viewsets.ViewSet):
    filter_backends = [filters.OrderingFilter]
    pagination_class = pagination.LimitOffsetPagination
    
    def create(self, request, *args, **kwargs):
        breakpoint()
        try:
            validated_data = PikachuObject(**request.data)
        except Exception as e:
            return Response(data=e.errors(), status=status.HTTP_400_BAD_REQUEST)
        pikachu_service = PikachuService()
        pikachu_instance = pikachu_service.create_pikachu(validated_data)
        pikachu_data = pikachu_service.retrieve_pikachu(pikachu_instance)
        return Response(data = json.loads(pikachu_data.model_dump_json()), status=status.HTTP_201_CREATED, content_type="application/json")

    def partial_update(self, request, pk=None, *args, **kwargs):
        try:
            pikachu_instance = Pikachu.objects.get(pk=pk)
        except Pikachu.DoesNotExist as e:
            return Response(data = None, status=status.HTTP_404_NOT_FOUND)
        pikachu_service = PikachuService()
        try:
            pikachu_object = pikachu_service.retrieve_pikachu(pikachu_instance)
            pikachu_data = pikachu_object.model_dump()
            pikachu_data = deep_update(pikachu_data, request.data)
            validated_data = PikachuObject(**pikachu_data)
        except Exception as e:
            return Response(data=e.errors(), status=status.HTTP_400_BAD_REQUEST)
        pikachu_instance = pikachu_service.update_pikachu(pikachu_instance.id, validated_data)
        pikachu_data = pikachu_service.retrieve_pikachu(pikachu_instance)
        return Response(data = json.loads(pikachu_data.model_dump_json()), status=status.HTTP_200_OK, content_type="application/json")
    
    def list(self, request):
        pikachu_service = PikachuService()
        pikachu_instances = Pikachu.objects.all()
        pikachu_objects_list = pikachu_service.list_pikachu(pikachu_instances)
        pikachu_objects_data = [json.loads(pikachu_data.model_dump_json()) for pikachu_data in pikachu_objects_list]
        response_data = {
            "count":pikachu_instances.count(),
            "results":pikachu_objects_data
        }
        return Response(data = response_data, status=status.HTTP_200_OK, content_type="application/json")
    
    def retrieve(self, request, pk=None):
        try:
            pikachu_instance = Pikachu.objects.get(pk=pk)
        except Pikachu.DoesNotExist as e:
            return Response(data = None, status=status.HTTP_404_NOT_FOUND)
        pikachu_service = PikachuService()
        pikachu_data = pikachu_service.retrieve_pikachu(pikachu_instance)
        return Response(data = json.loads(pikachu_data.model_dump_json()), status=status.HTTP_200_OK, content_type="application/json")

    def delete(self, request, pk=None):
        try:
            pikachu_instance = Pikachu.objects.get(pk=pk)
        except Pikachu.DoesNotExist as e:
            return Response(status=status.HTTP_404_NOT_FOUND)
        pikachu_service = PikachuService()
        pikachu_data = pikachu_service.delete_pikachu(pikachu_instance)
        return Response(status=status.HTTP_204_NO_CONTENT)