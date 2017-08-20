"""ask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin

from qa import views as qaviews

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', qaviews.test), # call the test (OK) function from views here!
    url(r'^signup/$', qaviews.test), # call the test (OK) function from views here!
    url(r'^question/(?P<qid>[0-9]+)$', qaviews.question_page, name='question'), # call the test (OK) function from views here! 
    url(r'^$', qaviews.index, name='index'), # call the test (OK) function from views here!
    url(r'^ask/$', qaviews.test), # call the test (OK) function from views here!
    url(r'^popular/', qaviews.popular, name='popular') # call the test (OK) function from views here!
    #url(r'^new/', qaviews.test) # call the test (OK) function from views here!
    
]
