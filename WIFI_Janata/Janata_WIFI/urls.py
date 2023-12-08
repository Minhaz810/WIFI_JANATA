
from django.contrib import admin
from django.urls import path
from TableView.views import your_view
from Dynamic_Table.views import Data,Add,AddRec,Delete,Update,Uprec
from chart.views import chart


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',your_view,name='home'),
    path('data/',Data,name='data'),
    path('add/',Add,name='add'),
    path('addrec/',AddRec, name='addrec'),
    path('data/delete/<int:id>/',Delete,name='Delete'),
    path('data/update/<int:id>/',Update,name="update"),
    path('uprec/<int:id>/',Uprec,name="uprec"),
    path('chart/',chart,name='chart')
]
