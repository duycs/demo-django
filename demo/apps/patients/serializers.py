from rest_framework import serializers

from .models import Patient


class PatientSerializer(serializers.ModelSerializer):
    # medical_record = serializers.CharField(db_index=True, max_length=255, unique=True)
    # name = serializers.CharField(db_index=True, max_length=255)
    # telephone_number = serializers.TextField()
    # insurer_DID = serializers.TextField()
    # insurered_symbol = serializers.TextField()
    # insurered_number = serializers.IntegerField()

    class Meta:
        model = Patient
        fields = ('medical_record', 'name', 'telephone_number', 'insurer_DID', 'insurered_symbol', 'insurered_number')
        read_only_fields = ('medical_record', 'insurer_DID', 'insurered_number')

    def create(self, validated_data):
        return Patient.objects.create_patient(**validated_data)
