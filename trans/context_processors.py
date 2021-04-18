from django.conf import settings

def ioi_settings(request):
    return {'settings': {
        'SITE_TITLE': 'APIO 2021 Translation Home Page',
        'CONTEST_TITLE': 'APIO 2021',
        'CONTEST_FULL_TITLE': 'Asia-Pacific Informatics Olympiad 2021',
        'CONTEST_DATE': '22 - 23 May 2021',
        'CONTEST_PLACE': 'Indonesia',
        'PRINT_ENABLED': settings.PRINT_ENABLED,
        'CUSTOM_PRINT_ENABLED': settings.CUSTOM_PRINT_ENABLED,
        'TIME_ZONE': settings.TIME_ZONE,
        'IMAGES_URL': '/media/images/',
    }}
