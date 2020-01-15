from rest_framework import serializers, status
from rest_framework.exceptions import NotFound
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Patient
from .renderers import PatientJSONRenderer
from .serializers import PatientSerializer


class PatientRetrieveAPIView(RetrieveAPIView):
    permission_classes = (AllowAny,)
    #queryset = Patient.objects.select_related('user')
    queryset = Patient.objects.all()
    renderer_classes = (PatientJSONRenderer,)
    serializer_class = PatientSerializer

    def retrieve(self, request, name, *args, **kwargs):
        # Try to retrieve the requested Patient and throw an exception if the
        # Patient could not be found.
        try:
            patient = self.queryset.get(name=name)
        except Patient.DoesNotExist:
            raise NotFound('A Patient with this name was not found.')

        serializer = self.serializer_class(patient, context={
            'request': request
        })

        return Response(serializer.data, status=status.HTTP_200_OK)


class CreatePatientAPIView(APIView):
    # Allow any user (authenticated or not) to hit this endpoint.
    permission_classes = (AllowAny,)
    renderer_classes = (PatientJSONRenderer,)
    serializer_class = PatientSerializer

    def post(self, request):
        patient = request.data.get('patient', {})
        serializer = self.serializer_class(data=patient)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)