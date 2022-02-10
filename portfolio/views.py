from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        data = {
            'name' : name,
            'email' : email,
            'subject' : subject,
            'message' : message,
        }

        message = '''
        New Message From {} ,
        
        Subject : {}

        Message : {} 

        sender-email : {}
        '''.format(data['name'],data['subject'],data['message'],data['email'])

        send_mail(data['subject'],message,'',['jaswanthproject1410@gmail.com'])

    return render(request,"pages/index.html")

