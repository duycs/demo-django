from django.conf.urls import url

from .views import CreatePatientAPIView, PatientRetrieveAPIView

app_name = 'patients'

urlpatterns = [
    url(r'^patients/?$', CreatePatientAPIView.as_view()),
    url(r'^patients/(?P<name>\w+)/?$', PatientRetrieveAPIView.as_view()),
]