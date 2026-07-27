from datetime import date

import requests
from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings


def matches(request):
    today = date.today().isoformat()
    url = f"https://{settings.TENNIS_API_URL}/tennis/v2/atp/fixtures/{today}"
    headers= {
        'x-rapidapi-key': settings.TENNIS_API_KEY,
        'x-rapidapi-host': settings.TENNIS_API_URL,
    }

    try:
        response = requests.get(url, headers=headers, timeout=10) # FIX: put url here instead settings.TENNIS_API_URL. this is pretty apparent don't know how i didn't catch it lol
        response.raise_for_status()
        data = response.json()
        fixtures = data.get("data", [])
        error = None
    except requests.RequestException as e:
        fixtures = []
        error = str(e)

    return render(request, "pages/matches.html", {
        "matches" : fixtures,
        "error" : error,
    })

