from django.shortcuts import render
import requests
# Create your views here.
def index(req):
    return render(req, 'index.html')

def generate_insult(req):
    r = requests.get('https://insultapi.vercel.app/api/generated')
    insult = r.text
    return render(req, 'insult.html', {'insult': insult})