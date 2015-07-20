from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth import authenticate, login
from django.template import RequestContext
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.viewsets import GenericViewSet
from imdb.models import UserProfile, Item
from imdb.serializers import UserSerializer, ItemSerializer
from rest_framework import mixins


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


def index(request):
    return HttpResponseRedirect('/imdb/login')


@login_required
def logged_in(request):
    return render_to_response('imdb/logged_in.html',
                              context_instance=RequestContext(request)
                              )
