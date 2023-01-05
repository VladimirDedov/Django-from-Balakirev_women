from django import forms
from django.core.exceptions import ValidationError

from .models import *

class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = 'Категория не выбрана'
    class Meta:
        model = Women# связь формы м моделью Women
        fields = ['title','id','content', 'photo', 'is_publisher','cat']#Какие поля отображать в форме
        widgets = {#Прописывание стилей для определнных полей
            'title': forms.TextInput(attrs={'class':'form-input'}),
            'content': forms.Textarea(attrs={'cols' : 60, 'rows':10})
        }

    #Пользовательские валидаторы полей
    def clean_title(self):
        title = self.clean_data['title']
        if len(title) > 200:
            raise ValidationError('Длина превышает 200 символов')
        return title