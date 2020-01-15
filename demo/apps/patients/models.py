from django.db import models

from demo.apps.core.models import TimestampedModel

class PatientManager(models.Manager):
    
    def create_patient(self, medical_record, name, telephone_number = None, insurer_DID = None, insurered_symbol = None, insurered_number = None):

        if medical_record is None:
            raise TypeError('Patient must have a medical_record.')

        if name is None:
            raise TypeError('Patient must have an name.')

        patient = self.model(medical_record = medical_record, name = name, telephone_number = telephone_number, insurer_DID = insurer_DID, insurered_symbol = insurered_symbol, insurered_number = insurered_number)
        patient.save()

        return patient

class Patient(TimestampedModel):
#class Patient(object):
    # def __init__(self, medical_record, name, telephone_number, insurer_DID = None, insurered_symbol = None, insurered_number = None):
    #     self.medical_record = medical_record
    #     self.name = name
    #     self.telephone_number = telephone_number
    #     self.insurer_DID = insurer_DID
    #     self.insurered_symbol = insurered_symbol
    #     self.insurered_number = insurered_number

    medical_record = models.CharField(db_index=True, max_length=255, unique=True)
    name = models.CharField(max_length=255)
    telephone_number = models.TextField()
    insurer_DID = models.TextField()
    insurered_symbol = models.TextField()
    insurered_number = models.IntegerField()

    # Use manager
    objects = PatientManager()

    # Relation to other models

    def __str__(self):
        return self.medical_record