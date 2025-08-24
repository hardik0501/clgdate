from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Profile, Crush, Friendship, ProfileView, UserQuestionnaire

# Get your custom User model
User = get_user_model()

# Register the User model to the admin panel only if not already registered
try:
    admin.site.register(User)
except admin.sites.AlreadyRegistered:
    pass

# Register other models
admin.site.register(Profile)
admin.site.register(Crush)
admin.site.register(Friendship)
admin.site.register(ProfileView)
admin.site.register(UserQuestionnaire)
