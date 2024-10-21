from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view()
def root_route(request):
    if settings.DEBUG:
        return Response({
            'message': 'My drf API, for my photo sharing website, social.',
        })
    else:
        return Response({
            'message': 'This is a production environment.',
        })