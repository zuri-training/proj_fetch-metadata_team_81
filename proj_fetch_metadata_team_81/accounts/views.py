from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib.auth import login
from django.core.mail import send_mail
from django.contrib.auth.models import User
from .forms import RegistrationForm, UserEditForm
from .tokens import account_activation_token





@login_required
def profile(request):
    return render(request,
                  'registration/redirect.html',
                  {'section':'profile'})


def index(request):
    return render(request, 'landingpage/index.html')

def accounts_register(request):
    if request.method == 'POST':
        registerForm = RegistrationForm(request.POST)
        if registerForm.is_valid():
            user = registerForm.save(commit=False)
            user.email = registerForm.cleaned_data['email']
            user.set_password(registerForm.cleaned_data['password'])
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            subject = 'Activate your Account'
            message = render_to_string('registration/verification.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            #user.email_user(subject=subject, message=message)
            send_mail(
                subject,
                message,
                'ajadimarvellousgo@gmail.com',['ajadimarvellousgo@gmail.com'],
                fail_silently=False
                )
            return HttpResponse('registered succesfully and activation sent')
    else:
        registerForm = RegistrationForm()
    return render(request, 'registration/signup.html', {'form': registerForm})


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('login')
    else:
        return render(request, 'registration/account_activation_invalid.html')