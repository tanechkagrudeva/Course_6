from django import forms
from sender.models import Client, MailingMessage


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('first_name', 'last_name', 'patronymic', 'email', 'comment',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class MailingMessageForm(forms.ModelForm):
    class Meta:
        model = MailingMessage
        fields = ('subject', 'body', 'client',)

    def clean_name(self):
        name = self.cleaned_data['name']
        if any(word in name.lower() for word in
               ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']):
            raise forms.ValidationError('Название продукта содержит запрещенные слова')
        return name

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'