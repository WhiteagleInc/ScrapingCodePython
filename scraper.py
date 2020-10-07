import requests
import lxml.html as html

HOME_URL = 'https://www.larepublica.co/'

XPATH_LINK_TO_ARTICLE = '//div[@class="news V_Title_Img"]/a/@href'
XPATH_TITLE = '//div[@class="mb-auto"]/h2/a[@class="empresasSect"]/text()'
XPATH_SUMMARY = '//div[@class="news empresasSect"]/div[@class="lead"]/p/text()'
XPATH_BODY = '//div[@class="news empresasSect"]/div[@class="html-content"]/p[not(@class)]/text()'


def parse_home():
    try:
        response = requests.get()
    except ValueError as ve:
        print(ve)


def run():
    parse_home()


if __name__ == '__main__':
    run()