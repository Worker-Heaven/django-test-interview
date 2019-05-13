from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader


def index(request):
    template = loader.get_template('clientapp/index.html')
    context = {}

    return HttpResponse(template.render(context, request))


def client_new(request):
    template = loader.get_template('clientapp/client_new.html')
    context = {
        'template_url': 'client_new',
        'label': 'Save',
        'client_id': 0,
    }

    if request.method == 'GET':
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect(reverse('index'))


def client_update(request, client_id):
    template = loader.get_template('clientapp/client_update.html')
    context = {
        'template_url': 'client_update',
        'label': 'Update',
        'client_id': client_id,
    }

    if request.method == 'GET':
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect(reverse('index'))
