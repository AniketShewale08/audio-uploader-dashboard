from django import forms

class AudioUploadForm(forms.Form):
    audio_files = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True, 'accept': 'audio/*'}), required=True)
