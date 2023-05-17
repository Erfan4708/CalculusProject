from django.views.generic import CreateView
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
# Create your views here.

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')
