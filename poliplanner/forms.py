from django import forms
from .models import  *
from django.forms.widgets import DateInput, TextInput

class FormSettings(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FormSettings, self).__init__(*args, **kwargs)
        # Here make some changes such as:
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'

class CustomUserForm(FormSettings):
    nusp = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    senha = forms.CharField(widget=forms.PasswordInput)
    widget = {
        'password': forms.PasswordInput(),
    }
    #profile_pic = forms.ImageField()

    def __init__(self, *args, **kwargs):
        super(CustomUserForm, self).__init__(*args, **kwargs)

        if kwargs.get('instance'):
            instance = kwargs.get('instance').admin.__dict__
            self.fields['password'].required = False
            for field in CustomUserForm.Meta.fields:
                self.fields[field].initial = instance.get(field)
            if self.instance.pk is not None:
                self.fields['password'].widget.attrs['placeholder'] = "Atualizar senha"

    def clean_email(self, *args, **kwargs):
        formEmail = self.cleaned_data['email'].lower()
        if self.instance.pk is None:  # Insert
            if CustomUser.objects.filter(email=formEmail).exists():
                raise forms.ValidationError(
                    "Esse e-mail já está registrado")
        else:  # Update
            dbEmail = self.Meta.model.objects.get(
                id=self.instance.pk).admin.email.lower()
            if dbEmail != formEmail:  # There has been changes
                if CustomUser.objects.filter(email=formEmail).exists():
                    raise forms.ValidationError("Esse e-mail já está registrado")

        return formEmail

    class Meta:
        model = CustomUser
        fields = ['nusp', 'first_name', 'last_name', 'email',  'password' ]


class AlunoForm(CustomUserForm):
    def __init__(self, *args, **kwargs):
        super(AlunoForm, self).__init__(*args, **kwargs)

    class Meta(CustomUserForm.Meta):
        model = Aluno
        fields = CustomUserForm.Meta.fields + \
            ['curso', 'subject']


class AdminForm(CustomUserForm):
    def __init__(self, *args, **kwargs):
        super(AdminForm, self).__init__(*args, **kwargs)

    class Meta(CustomUserForm.Meta):
        model = Admin
        fields = CustomUserForm.Meta.fields


class GerenteForm(CustomUserForm):
    def __init__(self, *args, **kwargs):
        super(GerenteForm, self).__init__(*args, **kwargs)

    class Meta(CustomUserForm.Meta):
        model = Gerente
        fields = CustomUserForm.Meta.fields + \
            ['curso']


class CursoForm(FormSettings):
    def __init__(self, *args, **kwargs):
        super(CursoForm, self).__init__(*args, **kwargs)

    class Meta:
        fields = ['name']
        model = Curso


class SubjectForm(FormSettings):

    def __init__(self, *args, **kwargs):
        super(SubjectForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Subject
        fields = ['name', 'professor', 'oferecimento']


class OferecimentoForm(FormSettings):
    def __init__(self, *args, **kwargs):
        super(OferecimentoForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Oferecimento
        fields = '__all__'
        widgets = {
            'start_year': DateInput(attrs={'type': 'date'}),
            'end_year': DateInput(attrs={'type': 'date'}),
        }

class AlunoEditForm(CustomUserForm):
    def __init__(self, *args, **kwargs):
        super(AlunoEditForm, self).__init__(*args, **kwargs)

    class Meta(CustomUserForm.Meta):
        model = Aluno
        fields = CustomUserForm.Meta.fields 

class GerenteEditForm(CustomUserForm):
    def __init__(self, *args, **kwargs):
        super(GerenteEditForm, self).__init__(*args, **kwargs)

    class Meta(CustomUserForm.Meta):
        model = Gerente
        fields = CustomUserForm.Meta.fields


class TarefaForm(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = ('title', 'subject' , 'content', 'deadline')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}), 
            'subject': forms.Select(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}), 
            'deadline': forms.TextInput(attrs={'class': 'form-control'}), 
        }

        subject = forms.ModelMultipleChoiceField(
            queryset = Subject.objects.all(),
            widget=forms.CheckboxSelectMultiple
        )

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('username','content')

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}), 
            'content': forms.Textarea(attrs={'class': 'form-control'}), 
        }
    