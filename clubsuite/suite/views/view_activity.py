from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import View
from django.urls import reverse
from django.contrib import messages
from suite.models import Club
from suite.forms import DivisionCreateForm, BudgetCreateForm

from guardian.shortcuts import get_perms
from django.core.exceptions import PermissionDenied

#importing the libraries we will need
import pandas as pd
import numpy as np
import urllib
from fake_useragent import UserAgent
import requests
import re
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup



class Activity(View, LoginRequiredMixin):


    def get(self, request, club_id, *args, **kwargs):

        template_name = 'suite/club_activity.html'
        club:Club = get_object_or_404(Club, pk=club_id)
        keyword= club.club_description + ' activities'
        html_keyword= urllib.parse.quote_plus(keyword)
        print(html_keyword)
        number_of_result=10
        google_url = "https://www.google.com/search?q=" + html_keyword + "&num=" + str(number_of_result)
        print(google_url)

        ua = UserAgent()
        response = requests.get(google_url, {"User-Agent": ua.random})
        soup = BeautifulSoup(response.text, "html.parser")
        result = soup.find_all('div', attrs = {'class': 'ZINbbc'})
        results=[re.search('\/url\?q\=(.*)\&sa',str(i.find('a', href = True)['href'])) for i in result if "url" in str(i)]

#this is because in rare cases we can't get the urls
        links=[i.group(1) for i in results if i != None]

        args = {'links':links, 'club':club}
        return render(request, 'club_activity.html',args)


  