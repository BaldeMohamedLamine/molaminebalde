from django import forms
from .models import Profile, SocialProfile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture', 'biography', 'contact_info']

class SocialProfileForm(forms.ModelForm):
    class Meta:
        model = SocialProfile
        fields = ['platform', 'url']
        widgets = {
            'url': forms.URLInput(attrs={'placeholder': 'http://'})
        }
