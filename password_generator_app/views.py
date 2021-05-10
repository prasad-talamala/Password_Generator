import random

from django.shortcuts import render


def home(request):
    return render(request, "home.html")


def password(request):
    length = int(request.GET.get("length"))
    capital = request.GET.get("capital")
    number = request.GET.get("number")
    special = request.GET.get("special")
    unique = request.GET.get("unique")

    alphabets = 'abcdefghiklmnopqrstuvwxyz'
    number_digits = '0123456789'
    special_chars = '!@#$%^&*();~><?/'

    final_list_strings = list(alphabets)

    if capital == "on":
        final_list_strings.extend(alphabets.upper())

    if number == "on":
        final_list_strings.extend(number_digits)

    if special == "on":
        final_list_strings.extend(special_chars)

    pwd = ""

    for i in range(length):
        pwd += random.choice(final_list_strings)

    return render(request, "password_file.html", {"password": pwd})
