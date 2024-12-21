from django.db import migrations

def transfer_profiles(apps, schema_editor):
    # Récupérer les anciens modèles
    OldProfile = apps.get_model('profiles', 'Profile')
    NewProfile = apps.get_model('profiles', 'Profile')

    # Copier les données de l'ancien modèle vers le nouveau
    for old_profile in OldProfile.objects.all():
        NewProfile.objects.create(
            user=old_profile.user,
            favorite_city=old_profile.favorite_city
        )

class Migration(migrations.Migration):
    dependencies = [
        ('profiles', '0001_initial'),
        ('oc_lettings_site', '0001_initial'),  # Remplace 'last_migration' par le nom exact
    ]

    operations = [
        migrations.RunPython(transfer_profiles),
    ]
