"""Manages the views for the bmi-calc app

This is part of a Django web server app that is used to create a static site in
mkdocs. It utilises several other functions git, github, env manipulation and 
mkdocs

Functions:
    index: placeholder
"""
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.contrib import messages
from django.conf import settings

import sys
from fnmatch import fnmatch
from typing import Any, TextIO

import app.functions.constants as c

sys.path.append(c.FUNCTIONS_APP)
from app.functions.bmi_calculator import BMICalculator

from .forms import BMIInputsForm


def index(request: HttpRequest) -> HttpResponse:
    """Index page

    Args:
        request (HttpRequest): request from user

    Returns:
        HttpResponse: for loading the correct webpage
    """
    context: dict[str, Any] = {}
    form: BMIInputsForm
    bmi: float = 0.0

    if not (request.method == "GET" or request.method == "POST"):
        return render(request, "405.html", std_context(), status=405)

    if request.method == "GET":
        context = {"form": BMIInputsForm()}

        return render(request, "bmi_inputs.html", context | std_context())

    elif request.method == "POST":
        form = BMIInputsForm(request.POST)
        if form.is_valid():
            weight = form.cleaned_data["weight"]
            height = form.cleaned_data["height"]
            bmi_calc = BMICalculator()
            bmi = bmi_calc.BMI(weight, height)
            messages.success(
                request,
                f"BMI calculated as {bmi:.2f}",
            )

            context = {"form": form}

            return render(
                request,
                "bmi_inputs.html",
                context | std_context(),
            )
        else:
            messages.error(request, "BMI input error")
            context = {"form": form}
            return render(request, "bmi_inputs.html", context | std_context())

    # Should never really get here, but added for mypy
    return render(request, "500.html", std_context(), status=500)


def std_context() -> dict[str, Any]:
    """Title

    Description

    Returns:
        dict[str,Any]: context that is comment across the different views
    """

    std_context_dict: dict[str, Any] = {}
    docs_available: bool = False

    docs_available = True

    std_context_dict = {
        # "START_AFRESH": settings.START_AFRESH,
        # "mkdoc_running": mkdoc_running,
        "docs_available": docs_available,
        "FORM_ELEMENTS_MAX_WIDTH": c.FORM_ELEMENTS_MAX_WIDTH,
    }

    return std_context_dict


def custom_404(request: HttpRequest, exception) -> HttpResponse:
    """Title

    Description

    Args:
        request (HttpRequest): request from user

    Returns:
        HttpResponse: for loading the correct webpage
    """

    return render(request, "404.html", context=std_context(), status=404)


def custom_405(request: HttpRequest, exception) -> HttpResponse:
    """Title

    Description

    Args:
        request (HttpRequest): request from user

    Returns:
        HttpResponse: for loading the correct webpage
    """

    return render(request, "405.html", context=std_context(), status=405)
