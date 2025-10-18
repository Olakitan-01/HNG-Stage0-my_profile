import requests

from django.shortcuts import render

# Create your views here.
from django_ratelimit.decorators import ratelimit
from django.http import JsonResponse
from datetime import datetime, timezone


def my_profile(request):
    user = {"email": "olanrewajuemma2023@gmail.com", 
            "name": "OLANREWAJU Emmanuel",
            "stack":"Python(django)"}
    timestamp = datetime.now(timezone.utc).isoformat()

    try:
        response = requests.get("https://catfact.ninja/fact", timeout=5)
        response.raise_for_status()
        data = response.json()
        fact = data.get("fact", "Cats are...")
    except requests.exceptions.RequestException:
        fact = "could not fetch cat fact at the moment"

    result = {
        "status": "success",
        "user": user,
        "timestamp": timestamp,
        "fact": fact
    }
    return JsonResponse(result, content_type="application/json")

@ratelimit(key='ip', rate='5/m', block=True)
def me(request):
    return JsonResponse({"message": "ok"})