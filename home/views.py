from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.http import HttpResponse

class HomeView(View):
    # template_name = 'home/home.html'

    def get(self, request, *args, **kwargs):
        import os
        from sendgrid import SendGridAPIClient
        from sendgrid.helpers.mail import Mail

        message = Mail(
            from_email=os.environ.get('ADMIN_EMAIL'),
            to_emails=os.environ.get('MY_EMAIL'),
            subject='Sending with Twilio SendGrid is Fun',
            html_content='<strong>and easy to do anywhere, even with Python</strong>')
        try:
            sg = SendGridAPIClient(os.environ.get('SG_KEY1'))
            response = sg.send(message)
            print(response.status_code)
            print(response.body)
            print(response.headers)
        except Exception as e:
            print(e.message)
        return HttpResponse("hellow")

def error_400(request, exception=None):
    return render(request, 'home/error_pages/400.html')


def error_403(request, exception=None):
    return render(request, 'home/error_pages/403.html')


def error_404(request, exception=None):
    return render(request, 'home/error_pages/404.html')


def error_500(request, exception=None):
    return render(request, 'home/error_pages/500.html')


"""

committttttttttttt

"""