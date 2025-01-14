from django.http import JsonResponse, HttpResponse
from .models import Report
from .tasks import scan_url_task, scan_ip_task, scan_domain_task, scan_hash_task


# View to get all reports
def get_reports(request):
    reports = Report.objects.order_by('-id')[:30].values()
    return JsonResponse(list(reports), safe=False)

def scan_ip(request, ip):
    result = scan_ip_task.delay(ip)
    return JsonResponse({'status': 'success'})

def scan_domain(request, domain):
    result = scan_domain_task.delay(domain)
    return JsonResponse({'status': 'success'})

def scan_hash(request, hashStr): # 'hash' is a built-in python function don't wanna overwrite that
    result = scan_hash_task.delay(hashStr)
    return JsonResponse({'status': 'success'})

def scan_url(request, url):
    result = scan_url_task.delay(url)
    return JsonResponse({'status': 'success'})

def home(request):
    return HttpResponse("Hello HTTP!")