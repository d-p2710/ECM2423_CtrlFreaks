from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.contrib import messages
from django.views import View
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.template import loader
from django.http import HttpResponse

from .models import Profile, Avatar, Item, OwnedItem
from .forms import RegisterForm, LoginForm, UpdateUserForm, UpdateProfileForm

# Backend functionality for page views

def home(request):
    # Allows the home page to grab the profile information for a user
    # No longer spits out an error message when the user isn't logged in
    marker = request.user.id
    data = Profile.objects.filter(user=marker).values
    context = {
        'data': data
    }
    return render(request, 'users/home.html', context)

def terms(request):
    return render(request, 'users/terms.html')

class RegisterView(View):
    form_class = RegisterForm
    initial = {'key': 'value'}
    template_name = 'users/register.html'

    def dispatch(self, request, *args, **kwargs):
        # Redirects to the home page if a user tries to access the register page while logged in
        if request.user.is_authenticated:
            return redirect(to='/')

        # Otherwise work as normal
        return super(RegisterView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            created_user = form.save()
            
            # zj274 create new default avatar object to link to profile
            default_categories = ["colour", "mouth", "eyes"]
            default_items = []
            for category in default_categories:
                item = get_list_or_404(Item, category=category, is_default_img=True)[0]
                default_items.append(item)
            user_profile = get_object_or_404(Profile, user=created_user)
            new_avatar = Avatar(profile=user_profile,
                                colour=default_items[0],
                                mouth=default_items[1],
                                eyes=default_items[2])
            # create objects to represent user's item (part) ownership
            for item in default_items:
                new_owned_item = OwnedItem(profile=user_profile, item=item)
                new_owned_item.save()
            new_avatar.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect(to='login')

        return render(request, self.template_name, {'form': form})

class CustomLoginView(LoginView):
    form_class = LoginForm

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')

        if not remember_me:
            # Session expiry set to 0 seconds so it will automatically close the session after the browser is closed.
            self.request.session.set_expiry(0)

            # Set session as modified to force data updates/cookie to be saved.
            self.request.session.modified = True

        # Otherwise browser session will be as long as the session cookie time "SESSION_COOKIE_AGE" defined in
        # settings.py
        return super(CustomLoginView, self).form_valid(form)


@login_required
def profile(request):
    return render(request, 'users/profile.html')

@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='users-profile')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'users/profile.html', {'user_form': user_form, 'profile_form': profile_form})

# Extraneous code, but provides a template for allowing view methods to grab profile information from the active user
#@login_required
#def get_data(request):
#    username = request.user.username
#    data = Profile.objects.filter(username=username).values_list('points_amount')
#    template = loader.get_template('home.html')
#    context = {
#        'points': data
#    }
#    return HttpResponse(template.render(context, request))