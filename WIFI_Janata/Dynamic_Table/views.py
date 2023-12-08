from django.shortcuts import render,redirect
from .models import JWData
from django.core.paginator import Paginator
from datetime import datetime
# 
# Create your views here.
def Data(request):
    alldata=JWData.objects.all()
    page_number=request.GET.get('page',1)
    paginator=Paginator(alldata,8)
   
    alldata_final=paginator.get_page(page_number)
    return render(request,'Data.html',{'alldata_final':alldata_final})

def Add(request):
    return render(request,'add_form.html')
def AddRec(request):
    date=datetime.strptime(request.POST['date'], '%Y-%m-%d').date()
    tradecode=request.POST['tradecode']
    high=float(request.POST['high'])
    low=float(request.POST['low'])
    open=float(request.POST['open'])
    close=float(request.POST['close'])
    volume=int(request.POST['volume'])

    alldata=JWData(Date=date,TradeCode=tradecode,High=high,Low=low,Open=open,Close=close,Volume=volume)
    alldata.save()
    return redirect("/data")
def Delete(request,id):
    alldata=JWData.objects.get(id=id)
    alldata.delete()
    return redirect("/data")
def Update(request,id):
    alldata=JWData.objects.get(id=id)
    return render(request,'update_form.html',{'update':alldata})
def Uprec(request,id):
    date=datetime.strptime(request.POST['date'], '%Y-%m-%d').date()
    tradecode=request.POST['tradecode']
    high=float(request.POST['high'])
    low=float(request.POST['low'])
    open=float(request.POST['open'])
    close=float(request.POST['close'])
    volume=int(request.POST['volume'])
    alldata=JWData.objects.get(id=id)
    alldata.Date=date
    alldata.TradeCode=tradecode
    alldata.High=high
    alldata.Low=low
    alldata.Open=open
    alldata.Close=close
    alldata.Volume=volume
    alldata.save()
    return redirect("/data")