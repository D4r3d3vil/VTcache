from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Report
import json
from .tasks import scan_url_task
import vt
from celery.result import AsyncResult
from time import sleep

client = vt.Client("7d25b6268590d04054141216f89a3e97a44195bf1275958ec2ec454d3d01a5da") # api key -- useless

# View to get all reports
def get_reports(request):
    reports = Report.objects.order_by('-id')[:30].values()
    return JsonResponse(list(reports), safe=False)

# View to get a specific record by ID
def get_report_by_id(request, report_id):
    try:
        report = Report.objects.get(id=report_id)
        return JsonResponse({
            'id': report.id,
            'date': report.date,
            'type': report.type,
            'result': report.result,
        })
    except Report.DoesNotExist:
        return JsonResponse({'error': 'Report not found'}, status=404)

# View to create a new report
def create_report(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        report = Report.objects.create(
            type=data.get('type'),
            result=data.get('result')
        )
        return JsonResponse({
            'id': report.id,
            'date': report.date,
            'type': report.type,
            'result': report.result,
        }, status=201)

def scan_url(request, url):
    result = scan_url_task.delay(url)
    task = AsyncResult(result.id)
    return HttpResponse('DOne')

def home(request):
    return HttpResponse("Hello HTTP!")