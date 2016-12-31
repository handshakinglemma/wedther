# get_weather
# Uses lxml and requests to get the temperature from Weather Canada.

from lxml import etree
from lxml import html
import requests

def get_weather():

    # Gets the current temperature.
    temperature_page = requests.get('https://weather.gc.ca/city/pages/ab-50_metric_e.html')
    temperature_tree = html.fromstring(temperature_page.content)
    temperature = temperature_tree.xpath('//span[@class="wxo-metric-hide"]/text()')[0]

    # Gets the current condition.
    picture_page = requests.get('https://weather.gc.ca/forecast/hourly/ab-50_metric_e.html')
    picture_tree = html.fromstring(picture_page.content)
    weather_str = picture_tree.xpath('.//p/text()')[0]

    # Print statement for testing.
    # print(temperature, weather_str)
    
    # Return the current temperature and weather condition.
    return [temperature, weather_str]

def get_alerts():

    # Get current alert message.
    alert_page = requests.get('https://weather.gc.ca/warnings/report_e.html?ab33')
    alert_tree = html.fromstring(alert_page.content)
    alert = alert_tree.xpath('//p/text()')[2]

    # Return the current alert message.
    return alert
