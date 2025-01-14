# tasks.py
from celery import shared_task
from .models import Report
import vt
import base64

client = vt.Client("7d25b6268590d04054141216f89a3e97a44195bf1275958ec2ec454d3d01a5da") # api key -- useless

@shared_task
def scan_url_task(url):
    try: # some characters in URL such as : and // are not allowed in urls so they must be decoded
        url = base64.urlsafe_b64decode(url).decode()
    except Exception as e:
        print('Invalid URL')
    result = client.scan_url(url).to_dict()
    analysis = client.get_json('https://www.virustotal.com/api/v3/analyses/'+result['id'])
    report = Report(type='url', result=analysis)
    report.save()

@shared_task
def scan_hash_task(hashStr): # 'hash' is a built-in function in python don't wanna overwrite that
    analysis = client.get_json('https://www.virustotal.com/api/v3/files/' + hashStr)
    report = Report(type='hash', result=analysis)
    report.save()

@shared_task
def scan_ip_task(address):
    analysis = client.get_json('https://www.virustotal.com/api/v3/ip_addresses/' + address)
    report = Report(type='ip', result=analysis)
    report.save()

@shared_task
def scan_domain_task(domain):
    analysis = client.get_json('https://www.virustotal.com/api/v3/domains/' + domain)
    report = Report(type='domain', result=analysis)
    report.save()