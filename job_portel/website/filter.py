import django_filters
from job.models import Job

class JobFiter(django_filters.FilterSet):
    title=django_filters.CharFilter(lookup_expr="icontains")
    class Meta:
        model =Job
        fields=[
            'title','state','job_type','industry'
        ]