# Generated by Django 5.1.1 on 2024-11-08 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salestrakav2', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$870000$Sah4Era8v1euqojBir81fz$XydAwI72lewWiZ1kGAA+NwT1XTj8x9mLGLbGQlyZip4=', max_length=128),
        ),
    ]
