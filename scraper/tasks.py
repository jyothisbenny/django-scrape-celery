from celery import shared_task
from requests_html import HTMLSession

from .models import ScrapeData

@shared_task
def scrape_and_save():
    url = 'https://geonode.com/free-proxy-list'
    s = HTMLSession()
    try:
        response = s.get(url)
        """sleet time is required to give enough time to load the data on website"""
        response.html.render(sleep=10)
        """free-proxies-table is a unique class id of the table"""
        table = response.html.find('.free-proxies-table', first=True)  # Adjust the selector as needed
        if table:
            """Loop through each row in the table
            Excluding first row since it is the header of the table """
            for row in table.find('tr')[1:]:
                columns = row.find('td')
                if columns:
                    ip = columns[0].text
                    port = columns[1].text
                    country = columns[2].text
                    protocols = columns[3].text
                    uptime = columns[7].text
                    ScrapeData.objects.create(ip=ip, port=port, protocol=protocols, country=country, uptime=uptime)
                    print(f"IP: {ip}, Port: {port}, country {country}, protocols: {protocols}, uptime: {uptime}")
        else:
            print("Table not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
