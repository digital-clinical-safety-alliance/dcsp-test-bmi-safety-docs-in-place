"""Form management for the Django dynamic site app

Classes:
    BMIInputForm: a form for BMI
"""

from django import forms
from django.conf import settings
import sys

from typing import Any

import app.functions.constants as c

sys.path.append(c.FUNCTIONS_APP)


def validation_response(
    self, field: str, valid: bool, error_message: str
) -> None:
    """A general function to create form validation results

    Provides the field class and error messages to work with Bootstrap.

    Args:
        field: name of field.
        valid: if the validation of the field passes, True = passes, False = does
               not pass.
        error_message: message to display if data does not pass validation.
    """
    if valid:
        self.fields[field].widget.attrs[
            "class"
        ] = f"form-control is-valid { c.FORM_ELEMENTS_MAX_WIDTH }"
    else:
        self.add_error(field, error_message)
        self.fields[field].widget.attrs[
            "class"
        ] = f"form-control is-invalid { c.FORM_ELEMENTS_MAX_WIDTH }"
    return


class BMIInputsForm(forms.Form):
    weight = forms.FloatField(
        required=False,
        min_value=0,
        max_value=300,
        widget=forms.NumberInput(
            attrs={
                "class": f"form-control { c.FORM_ELEMENTS_MAX_WIDTH }",
            }
        ),
    )

    height = forms.FloatField(
        required=False,
        min_value=0,
        max_value=300,
        widget=forms.NumberInput(
            attrs={
                "class": f"form-control { c.FORM_ELEMENTS_MAX_WIDTH }",
            }
        ),
    )
