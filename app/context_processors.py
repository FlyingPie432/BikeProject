from django.conf import settings


def contact(request):
    contact_information = {
        'hot_line': '+1234567890',
        'email_address': 'info@example.com',
        'location': '123 Street, City, Country'
    }
    return {'contact_information': contact_information}

