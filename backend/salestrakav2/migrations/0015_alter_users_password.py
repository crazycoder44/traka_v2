# Generated by Django 5.1.1 on 2025-03-11 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salestrakav2', '0014_users_groups_users_is_active_users_is_admin_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$870000$W5TsMDi8tHNmxCPdNmId44$Z8Po5KpBQBmYCcsw4UI6/2E1hnblcclatX/r4GCIa7U=', max_length=128),
        ),
    ]
