from .models import Profile


def create_profile_for_user(user, *, email_address=None, display_name=None):
    if display_name is None:
        display_name = user.username

    if email_address is None:
        email_address = user.email

    profile, created = Profile.objects.get_or_create(
        user=user,
        defaults={
            "display_name": display_name,
            "email_address": email_address,
        },
    )

    return profile
