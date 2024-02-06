from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from rest_framework import generics

from .forms import GuestFormForm
from .models import GuestForm
from .serializers import GuestFormSerializer


class GuestFormAPIView(generics.ListCreateAPIView):
    queryset = GuestForm.objects.all()
    serializer_class = GuestFormSerializer


class GuestFormView(FormView):
    template_name = 'guestformapi/guest_form.html'
    form_class = GuestFormForm
    success_url = reverse_lazy('guestformapi:guest_form_success')

    def form_valid(self, form):
        # Access form data using form.cleaned_data
        name = form.cleaned_data['name']
        entering = form.cleaned_data['entering']
        roll_id = form.cleaned_data['roll_id']
        contact = form.cleaned_data['contact']
        address = form.cleaned_data['address']
        purpose = form.cleaned_data['purpose']
        notes = form.cleaned_data['notes']

        guest_form_instance = form.save()

        return HttpResponseRedirect(self.success_url)


def success_view(request):
    return render(request, 'guestformapi/guest_form_success.html')























# from django.shortcuts import render
#
# # Create your views here.
# from .models import GuestForm
# from .serializers import GuestFormSerializer
# from rest_framework import generics
#
#
# class GuestFormView(generics.ListCreateAPIView):
#     queryset = GuestForm.objects.all()
#     serializer_class = GuestFormSerializer
# guestformapi/views.py
