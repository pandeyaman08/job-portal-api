from rest_framework import serializers
from .models import Job, Application


class JobSerializer(serializers.ModelSerializer):
    posted_by = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Job
        fields = [
            'id',
            'title',
            'description',
            'company_name',
            'location',
            'job_type',
            'salary',
            'posted_by',
            'created_at',
            'is_active',
        ]
        read_only_fields = ['posted_by', 'created_at']


class ApplicationSerializer(serializers.ModelSerializer):
    candidate = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Application
        fields = [
            'id',
            'job',
            'candidate',
            'resume',
            'cover_letter',
            'status',
            'applied_at',
        ]
        read_only_fields = ['candidate', 'status', 'applied_at']
