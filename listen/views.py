from django.shortcuts import render
from django.http import HttpResponse
from listen import theCode as ts
import argparse
import sounddevice as sd
import numpy  # Make sure NumPy is loaded before it is used in the callback
assert numpy  # avoid "imported but unused" message (W0611)

# Create your views here.

def index(request):
   print("Hello")
   #test = ts.Test()
   #test


   return HttpResponse("Listen")