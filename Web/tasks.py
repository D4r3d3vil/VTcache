# tasks.py
from celery import shared_task
from .models import Report

@shared_task
def scan_url_task(url):
    from .views import client  # Import the client here or wherever it's defined
    result = client.scan_url(url).to_dict()
    analysis = client.get_json('https://www.virustotal.com/api/v3/analyses/'+result['id'])
    report = Report(type='url', result=analysis)
    report.save()