
from http.client import  HTTPConnection
from http.server import  BaseHTTPRequestHandler,HTTPServer
import urllib.request


def parsing():
    key='Mpb2vh%2FkiADe0I%2B1mVP0MlW8TwXVBb%2Fbgi1yBrX36Yx4v6wDVgmaRZk9%2BvYNyh8%2FvSGbyx5tGExltmd9wfN%2FbQ%3D%3D'

    #depr=str(input("도착도시를 입력하세요: "))
    #arri=str(input("출발도시를 입력하세요: "))
    time=str(input("검색시간를 입력하세요:   ex)20170528"))
    url = 'http://openapi.airport.co.kr/service/rest/serviceLine/serviceLines'
    newurl=url+'?schStDate='+time+'&schEdDate='+time+'&schLineType=D&schAirport=GMP&serviceKey='+key
    data=urllib.request.urlopen(newurl).read()
    d=str(data,"utf-8")
    return extractBookData(d)

def extractBookData(strXml):
    from xml.etree import ElementTree
    tree = ElementTree.fromstring(strXml)
    # Book 엘리먼트를 가져옵니다.
    itemElements = tree.getiterator("item")  # return list type
    for item in itemElements:
        arriport=item.find('arp')
        min=item.find('time')
        deport=item.find('odp')
        if len(arriport.text) > 0 :
           print("출방공항: "+arriport.text+"소요시간: "+min.text+"도착공항: "+deport.text)


