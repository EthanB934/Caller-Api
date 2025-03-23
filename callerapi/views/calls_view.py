from rest_framework import serializers, viewsets, status
from rest_framework.response import Response
from callerapi.models import Calls

class CallsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calls
        fields = ("id", "number")

class CallsViewSet(viewsets.ViewSet):
    def create(self, request):
        call = Calls()
        call.number = request.data["number"]

        try:
            call.save()
            serializer = CallsSerializer(call, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as ex:
            return Response(ex, status=status.HTTP_400_BAD_REQUEST)
