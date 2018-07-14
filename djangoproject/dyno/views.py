from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.urls import reverse, reverse_lazy
from dyno.forms import ContactForm
from django.views.generic.edit import FormView
from dyno.utils.display_info import get_info
from dyno.utils.image_model import predict
from PIL import Image


# Create your views here.


class home(View):

    def get(self, request):
        return render(request, 'dyno/home.html')

class dashboard(View):

    def get(self, request):
        return render(request, 'dyno/dashboard.html')

    def post(self, request):
        pass #to be added later

class diagnose(View):

    def get(self, request):
        return render(request, 'dyno/diagnose.html')

    def post(self, request):

        file = request.FILES.get('file')
        print(file)
        save_path = str("/Users/leerodgers/Google Drive/codingprojects/dyno/DjangoWebApp/djangoproject/dyno/images/%s" %file)
        file = Image.open(file)
        file.save(save_path)
        #x = predict(file)
        #print(x)
        return HttpResponseRedirect(reverse('dyno:success'))

class ContactView(FormView):
    template_name = 'dyno/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('dyno:success')

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        name = form.cleaned_data['name']
        message = form.cleaned_data['message']
        get_info(name, message)
        return super().form_valid(form)

class success(View):
    def get(self, request):
        return HttpResponse("Thanks!")

class form(View):

    def get(self, request):
        return render(request, 'dyno/form.html')

    def post(self, request):

        name = request.POST.get('name')
        text = request.POST.get('text')

        print(name)
        print(text)

        return HttpResponseRedirect(reverse('dyno:success'))
