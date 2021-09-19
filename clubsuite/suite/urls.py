from django.conf.urls import url, include
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm  # easy registration
from django.contrib.auth import login, logout
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

import django.contrib.auth as auth

from . import views

urlpatterns = [
    url(r'^about', views.About.as_view(), name='about'),
    url(r'^$', views.Dashboard.as_view(), name='dashboard'),
    url(r'^club/create$', views.ClubCreate.as_view(), name='club_create'),
    url(r'^club/search$', views.ClubSearch.as_view(), name='club_search'),
    url(r'^club/(?P<club_id>[0-9]+)/event_create$', views.EventCreate.as_view(), name='event_create'),
    url(r'^club/(?P<club_id>[0-9]+)/event/(?P<event_id>[0-9]+)$', views.Event.as_view(), name='event'),
    url(r'^dashboard/club-manage$', views.ClubManage.as_view(), name='club_manage'),
    url(r'^club/(?P<club_id>[0-9]+)/roster$', views.ClubRoster.as_view(), name='club_roster'),
    url(r'^club/(?P<club_id>[0-9]+)/$', views.ClubView.as_view(), name='club_view'),
    url(r'^club/(?P<club_id>[0-9]+)/csv_upload', views.CSVUpload.as_view(), name='csv_upload'),
    url(r'^club/(?P<club_id>[0-9]+)/behaviour', views.Behaviour.as_view(), name='behaviour'),
    url(r'^club/(?P<club_id>[0-9]+)/join$', views.ClubJoin.as_view(), name='club_join'),
    url(r'^club/(?P<club_id>[0-9]+)/emails$', views.ClubEmails.as_view(), name='club_emails'),
    url(r'^club/(?P<club_id>[0-9]+)/join/handle_requests$', views.HandleJoinRequest.as_view(), name='handle_join_request'),
    url(r'^club/(?P<club_id>[0-9]+)/edit$', views.ClubEdit.as_view(), name='club_edit'),
    url(r'^club/(?P<club_id>[0-9]+)/event/(?P<event_id>[0-9]+)/edit$', views.EventEdit.as_view(), name='event_edit'),
    url(r'^club/(?P<club_id>[0-9]+)/budget$', views.Budget.as_view(), name='budget'),
    url(r'^club/(?P<club_id>[0-9]+)/activity', views.Activity.as_view(), name='activity'),
    url(r'^account', views.Account.as_view(), name='edit_profile'),
    url(r'^admin/', admin.site.urls),

      url(r'^reset-password/$', PasswordResetView.as_view(), {'template_name': 'registration/password_reset_form.html', 'post_reset_redirect': 'suite:password_reset_done', 'email_template_name': 'registration/password_reset_email.html'}, name='reset_password'),

    url(r'^reset-password/done/$', PasswordResetDoneView.as_view(), {'template_name': 'registration/password_reset_done.html'}, name='password_reset_done'),
    url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', PasswordResetConfirmView.as_view(), {'template_name': 'registration/password_reset_confirm.html', 'post_reset_redirect': 'suite:password_reset_complete'}, name='password_reset_confirm'),

    url(r'^reset-password/complete/$', PasswordResetCompleteView.as_view(),{'template_name': 'registration/reset_password_complete.html'}, name='password_reset_complete'),

    #user logout
    # user registration
    url('^', include('django.contrib.auth.urls')),
    # url('^$', auth.login, name='login'),
    url('^loggedout/$', auth.logout, name='loggedout'),
    #url('^$', views.view_index, name='login'),

    url(r'^register$', views.RegistrationView.as_view(), name='register'),
    url(r'^register/done$', PasswordResetDoneView.as_view(), {
            'template_name': 'registration/initial_done.html',
        }, name='register_done'),
    url(r'^register/password/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', PasswordResetConfirmView.as_view(), {
            'template_name': 'registration/initial_confirm.html',
            'post_reset_redirect': 'suite:register_complete',
        }, name='register_confirm'),
    url(r'^register/complete/$', PasswordResetCompleteView.as_view(), {
            'template_name': 'registration/initial_complete.html',
        }, name='register_complete'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
