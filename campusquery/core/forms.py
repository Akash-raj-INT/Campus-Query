from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Answer, Comment, MentorProfile, Note, Question

class NoteForm(forms.ModelForm):
    ALLOWED_EXTENSIONS = {'.pdf', '.doc', '.docx', '.txt', '.ppt', '.pptx'}

    class Meta:
        model = Note
        fields = ['title', 'subject', 'file']
        widgets = {
            'file': forms.FileInput(
                attrs={'accept': '.pdf,.doc,.docx,.txt,.ppt,.pptx'}
            )
        }

    def clean_file(self):
        uploaded_file = self.cleaned_data['file']
        filename = uploaded_file.name.lower()
        if not any(filename.endswith(ext) for ext in self.ALLOWED_EXTENSIONS):
            raise ValidationError(
                'Unsupported file type. Upload PDF, DOC, DOCX, TXT, PPT, or PPTX.'
            )
        return uploaded_file

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'description']

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']


class MentorProfileForm(forms.ModelForm):
    class Meta:
        model = MentorProfile
        fields = ['department', 'expertise', 'bio', 'is_available']


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
