from django.http import HttpResponsePermanentRedirect
from convertx.constants import DOMAIN_NAME_WWW, DOMAIN_NAME_HTTPS


class RedirectToNonWwwMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        host = request.get_host().partition(':')[0]
        if host == DOMAIN_NAME_WWW:
            print(host)
            print(DOMAIN_NAME_WWW)
            print(DOMAIN_NAME_HTTPS + request.path)
            return HttpResponsePermanentRedirect(
                DOMAIN_NAME_HTTPS + request.path
            )
        else:
            return self.get_response(request)