from django.db import migrations

def transfer_lettings(apps, schema_editor):
    # Récupérer les anciens modèles
    OldAddress = apps.get_model('lettings', 'Address')
    OldLetting = apps.get_model('lettings', 'Letting')

    NewAddress = apps.get_model('lettings', 'Address')
    NewLetting = apps.get_model('lettings', 'Letting')

    # Copier les données des adresses
    address_mapping = {}
    for old_address in OldAddress.objects.all():
        new_address = NewAddress.objects.create(
            number=old_address.number,
            street=old_address.street,
            city=old_address.city,
            state=old_address.state,
            zip_code=old_address.zip_code,
            country_iso_code=old_address.country_iso_code
        )
        address_mapping[old_address.id] = new_address

    # Copier les données des locations
    for old_letting in OldLetting.objects.all():
        NewLetting.objects.create(
            title=old_letting.title,
            address=address_mapping[old_letting.address_id]
        )

class Migration(migrations.Migration):
    dependencies = [
        ('lettings', '0001_initial'),
        ('oc_lettings_site', '0001_initial'),  # Remplace 'last_migration' par le nom exact
    ]

    operations = [
        migrations.RunPython(transfer_lettings),
    ]
