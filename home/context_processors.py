from .models import UserProfile


def user_settings(request):
    """Make user preferences (theme, font, color) available in ALL templates."""
    settings = {
        'user_theme': 'light',
        'user_font': 'default',
        'user_color': 'orange',
    }

    if request.user.is_authenticated:
        try:
            profile = request.user.profile
            settings['user_theme'] = profile.theme
            settings['user_font'] = profile.font_size
            settings['user_color'] = profile.color_scheme
        except UserProfile.DoesNotExist:
            # Auto-create profile if missing
            profile = UserProfile.objects.create(user=request.user)
            settings['user_theme'] = profile.theme
            settings['user_font'] = profile.font_size
            settings['user_color'] = profile.color_scheme

    return settings