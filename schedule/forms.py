from django import forms
from .models import Teacher, TeacherInfo


class TeacherForm(forms.Form):
    first_name = forms.CharField(
        max_length=50,
        label="имя",
        help_text="введите имя преподавателя",
        widget=forms.TextInput(attrs={'placeholder': 'например: иван'})
    )

    last_name = forms.CharField(
        max_length=50,
        label="фамилия",
        help_text="введите фамилию преподавателя",
        widget=forms.TextInput(attrs={'placeholder': 'например: петров'})
    )

    email = forms.EmailField(
        label="email",
        help_text="введите электронную почту",
        widget=forms.EmailInput(attrs={'placeholder': 'mail@example.com'})
    )

    hire_date = forms.DateField(
        label="дата найма",
        help_text="формат ГГГГ-ММ-ДД",
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=False  # необязательное поле
    )

    salary = forms.DecimalField(
        label="зарплата",
        help_text="укажите зарплату (можно пропустить)",
        required=False,  # необязательное поле
        widget=forms.NumberInput(attrs={'placeholder': '0.00'})
    )

    is_active = forms.BooleanField(
        label="активен",
        help_text="отметьте если преподаватель активен",
        required=False,
        initial=True
    )

    # поля для TeacherInfo
    phone = forms.CharField(
        max_length=20,
        label="телефон",
        help_text="контактный телефон",
        required=False,
        widget=forms.TextInput(attrs={'placeholder': '+7...'})
    )

    birth_date = forms.DateField(
        label="дата рождения",
        help_text="формат ГГГГ-ММ-ДД",
        required=False,
        widget=forms.DateInput(attrs={'type': 'date'})
    )

    experience_years = forms.IntegerField(
        label="стаж (лет)",
        help_text="сколько лет преподает",
        required=False,
        widget=forms.NumberInput(attrs={'placeholder': '0'})
    )

    bio = forms.CharField(
        label="биография",
        help_text="краткая информация",
        required=False,
        widget=forms.Textarea(attrs={'rows': 4, 'placeholder': 'расскажите о преподавателе...'})
    )