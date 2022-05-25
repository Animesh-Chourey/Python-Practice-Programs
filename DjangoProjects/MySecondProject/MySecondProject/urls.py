"""MySecondProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from FirstApp import views
from SecApp import views as v
from ThirdApp import views as t
urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/',views.my_view),
    path('',views.f_view),
    path('demo/',v.sec_view),
    path('Sum/<int:a>/<int:b>',v.sum),
    #path('Sum/<a>/<b>/',v.sum), here data will be taken as string and will be concatenated as result
    path('show/<str:fname>/<str:lname>/',v.show),
    path('qstr/',v.queryStr),
    path('pstr/',v.query_P_Str),
    path('mytemp/',t.tempDemo),
    path('mydate/',t.dateDemo),
    path('myloop/',t.loopDemo),
    path('mydict/',t.dictDemo),
    path('myif/',t.ifDemo),
    path('mymax/',t.maxDemo),
    path('myDictTest/',t.dictTest),
]
