from rest_framework.generics import ListAPIView
from .serializers import ReportedFileSerializer, UploadedFileSerializer
from reporter.models import ReportedFile
from loader.models import UploadedFile

class ReportedFileList(ListAPIView):
    serializer_class = ReportedFileSerializer

    def get_queryset(self):
        query_params = self.request.query_params.dict()
        count = query_params['count'] if 'count' in query_params else 2
        page = query_params['page'] if 'page' in query_params else 1
        lower_lim = (page - 1)*count
        higher_lim = lower_lim + count
        return ReportedFile.objects.all().order_by('-generate_date')[lower_lim:higher_lim]

class UploadedFileList(ListAPIView):
    serializer_class = UploadedFileSerializer

    def get_queryset(self):
        query_params = self.request.query_params.dict()
        count = query_params['count'] if 'count' in query_params else 3
        page = query_params['page'] if 'page' in query_params else 1
        lower_lim = (page - 1)*count
        higher_lim = lower_lim + count
        return UploadedFile.objects.all().order_by('-upload_date')[lower_lim:higher_lim]