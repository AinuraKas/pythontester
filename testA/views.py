from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse
from django.template import loader
from . import models, db_views
import random
from django.db.models import Sum
from django.views.generic import ListView, CreateView, UpdateView

app_name = 'testA'


def index(request):
    kafedras = models.Kafedra.objects.all()
    predms = models.Predm.objects.all()
    template = loader.get_template('testA/index.html')
    context = {
        'kafedras': kafedras,
        'predms': predms,

    }
    return HttpResponse(template.render(context, request))


def DisInKaf(request, IdKaf):
    predms = models.Predm.objects.filter(idkaf=IdKaf)
    template = loader.get_template('testA/dicsinkaf.html')
    context = {

        'predms': predms,

    }
    return HttpResponse(template.render(context, request))


def TestInKaf(request, Idpredm):
    tests = models.Test.objects.filter(idpredm=Idpredm)
    template = loader.get_template('testA/tests.html')
    context = {

        'tests': tests,

    }
    return HttpResponse(template.render(context, request))


def Questions(request, Idtest):
    tests = db_views.fullyVopros.objects.filter(fv_idtest=Idtest).values_list('fv_idvopr', flat=True)
    test1 = random.sample(list(tests), 15)
    testitog = db_views.fullyVopros.objects.filter(fv_idvopr__in=test1)

    template = loader.get_template('testA/que.html')
    context = {

        'testitog': testitog,


    }
    return HttpResponse(template.render(context, request))

def CcntCorrectAnsw(request, Idvopr):
    otvcorr = models.Otvet.objects.filter(idvopr=Idvopr, ball__gt=0).count()
    template = loader.get_template('testA/que.html')
    context = {

        'otvcorr': otvcorr,

    }
    return HttpResponse(template.render(context, request))


def vote(request,questions_id):
    try:
        questions_id += "0"
        v = [int(s) for s in questions_id.split(',')]

        otvcorr = models.Otvet.objects.filter(idotvet__in=v).aggregate(Sum('ball'))
        return HttpResponse("You're results %s."%otvcorr['ball__sum'] )
    except():
        return HttpResponse("error")