from django import forms
from django.core.exceptions import ValidationError
# from django.core.validators import validate_slug
import re
# Create your models here.


def validator_title(title):
    pattern = "[a-zA-Z0-9\\s]+"
    if re.match(pattern, title):
        print("validate success")
    else:
        print("validate fail")
        raise ValidationError(
            message="Format of name is [a-zA-Z0-9\\s]+",
            params={"values": title}
        )


class UploadFileForm(forms.Form):
    # title = forms.CharField(max_length=255, validators=[validate_slug])
    title = forms.CharField(max_length=255, validators=[validator_title])
    file = forms.FileField()
