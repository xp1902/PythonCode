from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'url', 'content']

        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': "名字",
            }),
            'email': forms.TextInput(attrs={
                'placeholder': "邮箱",
            }),
            'url': forms.TextInput(attrs={
                'placeholder': "网址",
            }),
            'content': forms.Textarea(attrs={
                'placeholder': '我来评两句~'}),
        }

