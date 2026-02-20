from rest_framework import generics, permissions
from .models import Job, Application
from .serializers import JobSerializer, ApplicationSerializer
from .permissions import IsRecruiter, IsCandidate
class JobListView(generics.ListAPIView):
    queryset = Job.objects.filter(is_active=True).order_by('-created_at')
    serializer_class = JobSerializer
    permission_classes = [permissions.AllowAny]

class JobDetailView(generics.RetrieveAPIView):
    queryset = Job.objects.filter(is_active=True)
    serializer_class = JobSerializer
    permission_classes = [permissions.AllowAny]

class JobCreateView(generics.CreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [IsRecruiter]

    def perform_create(self, serializer):
        serializer.save(posted_by=self.request.user)

class ApplyJobView(generics.CreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = [IsCandidate]

    def perform_create(self, serializer):
        serializer.save(candidate=self.request.user)


