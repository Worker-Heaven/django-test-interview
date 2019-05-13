from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader

from .models import Client


def index(request):
    template = loader.get_template('clientapp/index.html')

    clients = Client.objects.all()
    context = {
        'clients': clients,
    }

    return HttpResponse(template.render(context, request))


def client_new(request):
    template = loader.get_template('clientapp/client_new.html')
    context = {
        'label': 'Add',
    }

    if request.method == 'GET':
        return HttpResponse(template.render(context, request))
    else:
        full_name = request.POST['full_name']
        contact_name = request.POST['contact_name']
        address = request.POST['address']
        email_address = request.POST['email_address']
        phone_number = request.POST['phone_number']

        if len(full_name) > 0 and len(email_address) > 0 and len(phone_number) > 0:
            client = Client(
                full_name=full_name,
                contact_name=contact_name,
                address=address,
                email_address=email_address,
                phone_number=phone_number,
            )

            client.save()

            return HttpResponseRedirect(reverse('index'))

        else:
            context = {
                'label': 'Add',
                'full_name': full_name,
                'address': address,
                'contact_name': contact_name,
                'email_address': email_address,
                'phone_number': phone_number,
            }

            return HttpResponse(template.render(context, request))


def client_update(request, client_id):
    template = loader.get_template('clientapp/client_update.html')

    clientInfo = Client.objects.get(pk=client_id)
    context = {
        'label': 'Update',
        'client_id': client_id,
        'full_name': clientInfo.full_name,
        'address': clientInfo.address,
        'contact_name': clientInfo.contact_name,
        'email_address': clientInfo.email_address,
        'phone_number': clientInfo.phone_number,
    }

    if request.method == 'GET':
        return HttpResponse(template.render(context, request))
    else:
        full_name = request.POST['full_name']
        contact_name = request.POST['contact_name']
        address = request.POST['address']
        email_address = request.POST['email_address']
        phone_number = request.POST['phone_number']

        if len(full_name) > 0 and len(email_address) > 0 and len(phone_number) > 0:
            clientInfo.full_name = full_name
            clientInfo.address = address
            clientInfo.contact_name = contact_name
            clientInfo.email_address = email_address
            clientInfo.phone_number = phone_number

            clientInfo.save()

            return HttpResponseRedirect(reverse('index'))

        else:
            context = {
                'label': 'Add',
                'full_name': full_name,
                'address': address,
                'contact_name': contact_name,
                'email_address': email_address,
                'phone_number': phone_number,
            }

            return HttpResponse(template.render(context, request))
