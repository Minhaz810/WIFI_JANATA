import os
from django.shortcuts import render
from django.conf import settings
from django.core.paginator import Paginator
from Dynamic_Table.models import JWData
def your_view(request):
   
    
      
        json_data = JWData.objects.all()
        page=request.GET.get('page',1)
        paginator=Paginator(json_data,10)
   
        json_data_final=paginator.get_page(page)
        


        return render(request, 'Home.html', {'json_data': json_data_final})
