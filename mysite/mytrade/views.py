from django.shortcuts import render
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup



# Create your views here.
def index(request):
    response = requests.get('http://nipper.work/btc/index.php?market=bitFlyer&coin=BTCJPY&periods=86400&after=1420070400')
    bs = BeautifulSoup(response.text, "html.parser")
    value = bs.find_all("td")
    lists = []
    num = int(len(value)/6)
    for i in range(int(len(value)/6)):
        li = []
        for j in range(6):
            li.append(value[-(i*6+j)-1].get_text())
        lists.append(li)
    
        
    
    context = {"value":lists,"num":num}
    return render(request,"mytrade/index.html",context)
def results(request):
    return HttpResponse("This is result")
