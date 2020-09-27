from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from .algorithms.decryption import decrypt
from .algorithms.graph import find_node
from .algorithms.get_marked import get_marked
from .algorithms.data import g
import json
# Create your views here.
class home(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')
    def get(self, request):
        return render(request, 'core/index.html')
    def post(self, request):
        #Load input from frontend
        encrypted_text = request.POST['encrypted_text']
        key = request.POST['key'].upper()
        graph = g
        if request.POST['graph'].strip() != '':
            graph = json.loads(request.POST['graph'].lower())
        #Process input
        decrypted_text = decrypt(encrypted_text, key)
        marked = get_marked(graph, decrypted_text.lower())
        location = find_node(graph, marked)
        #Add output to session
        request.session['encrypted_text'] = encrypted_text
        request.session['location'] = location
        request.session['decrypted_text'] = decrypted_text
        return redirect(reverse_lazy('output'))
class output(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'core/output.html')

class login(LoginView):
    template_name = "core/login.html"

class logout(LogoutView):
    next_page = reverse_lazy('login')