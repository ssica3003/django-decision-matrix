"""ddm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic.base import RedirectView

from ddm import defaults

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^options/', include('ddm.options.urls', namespace='options')),
    url(r'^criteria/', include('ddm.criteria.urls', namespace='criteria')),
    url(r'^categories/', include('ddm.categories.urls', namespace='categories')),
    url(r'^weighting/', include('ddm.weighting.urls', namespace='weighting')),
    url(r'^scoring/', include('ddm.scoring.urls', namespace='scoring')),
    url(r'^printing/', include('ddm.printing.urls', namespace='printing')),
    url(r'^', include('ddm.dashboard.urls', namespace='dashboard'))
]
