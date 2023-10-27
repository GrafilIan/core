from django import forms
from .models import Announcement
class AnnouncementForm(forms.ModelForm):
    announcement_list = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'summernote-simple',  # Add necessary CSS classes
            'placeholder': 'Title',  # Set the placeholder text
            'required': 'True',
        })
    )

    class Meta:
        model = Announcement
        fields = ['announcement_list', 'image_announcement', 'document_announcement']

    def __init__(self, *args, **kwargs):
        super(AnnouncementForm, self).__init__(*args, **kwargs)
        self.fields['image_announcement'].widget.attrs.update({
            'class': 'form-group',  # Add necessary CSS classes
            'placeholder': 'Thumbnail',  # Set the placeholder text
            'required': False
        })
        self.fields['document_announcement'].widget.attrs.update({
            'class': 'form-control',  # Add necessary CSS classes
            'placeholder': 'Document',  # Set the placeholder text
            'required': False
        })