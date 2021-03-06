"""
Forms that use the models to add and modify entries in the database.
"""
from django import forms
from django.forms import ModelForm

from PepBandWebsite.models import Song, eBoard, Section


class addSong(forms.ModelForm):
    """
    Adds a song to the database
    """
    title = forms.CharField(required=True)
    public = forms.BooleanField(required=True)
    video = forms.CharField(required=False)

    class Meta:
        model = Song
        fields = ("title", "public")

    def save(self, commit=True):
        entry = Song()
        entry.title = self.cleaned_data['title']
        entry.public = self.cleaned_data['public']
        entry.video = self.cleaned_data['video']

        if commit:
            entry.save()
        return entry


class changeSong(forms.ModelForm):
    """
    Changes the fields for a song
    """
    notes = forms.CharField(required=True)

    class Meta:
        model = Song
        fields = ('notes',)



class changeEBoard(ModelForm):
    """
    Change the fields for a selected eboard member in the database
    """
    firstName = forms.CharField(required=True)
    lastName = forms.CharField(required=True)
    cell = forms.RegexField(regex=r'^\+?1?\d{9,15}$', required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = eBoard
        fields = ('firstName', 'lastName', 'cell', 'email')


class changeSection(forms.ModelForm):
    """
    Changes the fields for a section leader in the database
    """
    firstName = forms.CharField(required=True)
    lastName = forms.CharField(required=True)
    cell = forms.RegexField(regex=r'^\+?1?\d{9,15}$', required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = Section
        fields = ('firstName', 'lastName', 'cell', 'email')

    def save(self, commit=True, instance=None):
        entry = Song()
        entry.firstName = self.cleaned_data['firstName']
        entry.lastName = self.cleaned_data['lastName']
        entry.cell = self.cleaned_data['cell']
        entry.email = self.cleaned_data['email']

        if commit:
            entry.save()

        return entry
