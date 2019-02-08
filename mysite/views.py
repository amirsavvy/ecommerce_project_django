from django.contrib.auth import authenticate, login, get_user_model
from django.shortcuts import render, redirect
from django.http import HttpResponse
from mysite.forms import ContactForm, LoginForm, RegisterForm

# Create your views here.
def home_page(request):
    # f_name = request.session.get('f_name', 'Unknown') # Session Getter
    # f_name = request.session['f_name'] # give error if null
    # print(f_name)

    context = {'title': "Home Page"}
    if request.user.is_authenticated:
        context['premium_content'] = "Mian Amir Savvy"

    return render(request, "home_page.html", context)

def about_page(request):
    context = {'title': "About Page"}
    return render(request, "home_page.html", context)

def contact_page(request):
    contact_form = ContactForm(request.POST, None)
    context = {
    'title': "Contact Page",
    'form': contact_form,
    'brand': 'My Brand Name'}

    if contact_form.is_valid():
        print(contact_form.cleaned_data)
        #  if request.method == 'POST':

        # print(request.POST)
        # print(request.POST.get('fullname'))
        # print(request.POST.get('email'))
        # print(request.POST.get('content'))

    return render(request, "contact/view.html", context)


def login_page(request):
    form = LoginForm(request.POST or None)
    context = {'form': form}
    print("User logged in")
    print(request.user.is_authenticated)
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # context['form'] = LoginForm()
            print("User is now validated and logedin")
            print(request.user.is_authenticated)
            login(request, user)
            return redirect('/')

        else:
            context['form'] = LoginForm()
            print("Error: user is not validated and logedin")

    return render(request, 'auth/login_page.html', context)

User = get_user_model()

def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {'form': form}
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        new_user = User.objects.create_user(username, email, password)
        print(new_user)

    return render(request, 'auth/register_page.html', context)
