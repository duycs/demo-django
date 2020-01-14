from demo.apps.core.renderers import demoJSONRenderer


class PatientJSONRenderer(demoJSONRenderer):
    object_label = 'patient'
    pagination_object_label = 'patients'
    pagination_count_label = 'patientsCount'
