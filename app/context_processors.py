from django.conf import settings

from django.conf import settings
from django.shortcuts import render


def contact(request):
    contact_information = settings.CONTACT_INFORMATION
    return render(request, 'contacts.html', {'contact_information': contact_information})
