from django.shortcuts import render
from Dynamic_Table.models import JWData

def chart(request):
    if 'TradeCode' in request.GET:
        selected_trade_code = request.GET['TradeCode']
        data = JWData.objects.filter(TradeCode=selected_trade_code)
        volume=[int(item.Volume) for item in data]
        date=[str(item.Date) for item in data]
        close=[float(item.Close) for item in data]
        return render(request, 'chart.html', {'date': date,'close':close,'volume':volume})
    else:
        default_data = JWData.objects.filter(TradeCode='1JANATAMF')
        default_volume=[int(item.Volume) for item in default_data]
        default_date=[str(item.Date) for item in default_data]
        default_close=[float(item.Close) for item in default_data]
        return render(request, 'chart.html', {'date': default_date,'close':default_close,'volume':default_volume})