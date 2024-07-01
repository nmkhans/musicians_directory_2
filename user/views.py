from django.urls import reverse_lazy
from .forms import UserRegisterForm
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.contrib import messages
from django.shortcuts import redirect

# Create your views here.
class UserRegisterView(CreateView):
  template_name = 'user/user_registration.html'
  form_class = UserRegisterForm
  success_url = reverse_lazy('home')

  def form_valid(self, form):
    messages.success(self.request, 'Account created. Login to continue.')
    return super().form_valid(form)
  
class UserLoginView(LoginView):
  template_name = 'user/user_login.html'

  def form_valid(self, form):
    messages.success(self.request, 'Login successfull.')
    return super().form_valid(form)
  
  def get_success_url(self):
    return reverse_lazy('home')
  
def user_logout(req):
  logout(req)
  messages.warning(req, 'Logout successfull')
  return redirect('home')