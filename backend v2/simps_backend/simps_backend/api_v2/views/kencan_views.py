
from django.http.response import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from simps_backend.api_v2.serializers.kencan_serializer import KencanCreateUpdateSerializer, KencanSerializer, StatusKencanSerializer

from simps_backend.api_v2.services.kencan_service import createKencan, deleteKencanById, getAllKencan, getAllStatusKencan, getKencanById, updateKencanById

# Status KencanView
class StatusKencanView(APIView):
    def get(self, request, format=None):
        try :
            query = getAllStatusKencan() 
            serializer = StatusKencanSerializer(query, many=True)
        except :
            raise Http404
       
        return Response(serializer.data)

"""
@params APIView
Request dan Response controller

@endpoints /kencan/
"""
class KencanView(APIView):
    def get(self, request, format=None):
        try :
            query = getAllKencan() 
            serializer = KencanSerializer(query, many=True)
        except :
            raise Http404
       
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = KencanCreateUpdateSerializer(data=request.data)
        
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


        createKencan(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


"""
@params APIView
Request dan Response controller

@endpoints /kencan/<int>/
"""
class KencanDetailView(APIView):
    def get(self, request, pk, format=None):
        try :
            query = getKencanById(pk)
            serializer = KencanSerializer(data=query[0].__dict__)
        except IndexError:
            raise Http404


        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


        return Response(serializer.data, status=status.HTTP_200_OK)
            

    def delete(self, request, pk, format=None):
        try :
            deleteKencanById(pk)
        except IndexError:
            raise Http404

        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk, format=None):
        serializer = KencanCreateUpdateSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        try:
            updateKencanById(pk, serializer.data)
        except IndexError:
            raise Http404

        return Response(serializer.data)
