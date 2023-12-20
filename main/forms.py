from django import forms
from .models import EntityModel
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class EntityModelForm(forms.ModelForm):
    reg_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), input_formats=['%Y-%m-%d'])

    class Meta:
        model = EntityModel
        exclude = ['date_added']

    def clean_legal_code(self):
        legal_code = self.cleaned_data.get('legal_code')
        if not legal_code.isdigit():
            raise ValidationError(_('Код повинен бути числовим значенням.'))

        return legal_code

    def clean_legal_fund(self):
        legal_fund = self.cleaned_data.get('legal_fund')
        if legal_fund < 0:
            raise ValidationError(_('Розмір фонду не може бути від\'ємним.'))

        return legal_fund

    def clean_legal_phone(self):
        legal_phone = self.cleaned_data.get('legal_phone')
        if legal_phone and not legal_phone.isdigit():
            raise ValidationError(_('Телефон повинен містити тільки цифри.'))

        return legal_phone
