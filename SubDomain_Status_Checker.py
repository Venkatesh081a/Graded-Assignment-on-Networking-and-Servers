import requests
import schedules
import time
from tabulate import tabulate

# List of sample sub-domains
subdomains=["blog.example.com","www.example.com","mail.example.com"]

def check_status():
    status_list = []
    for  subdomain in subdomains:
        try :
            response = requests.get("http://" + subdomain)
            status_list.append([subdomain,response.status_code])
        except requests.exceptions.RequestException:
            status_list.append([subdomain,"DOWN"])
    print(tabulate(status_list,headers=["Subdomain", "Status"], tablefmt="grid"))
    
# Schedule the  job to run every minute
schedule.every(1).minutes.do(check_status)

while True:
    schedule.run_pending()
    time.sleep(1)