import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(model_name='student', old_name='prenom', new_name='first_name'),
        migrations.RenameField(model_name='student', old_name='nom', new_name='last_name'),
        migrations.RemoveField(model_name='student', name='age'),
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['last_name', 'first_name']},
        ),
        migrations.AlterField(
            model_name='student',
            name='first_name',
            field=models.CharField(max_length=100, verbose_name='prénom'),
        ),
        migrations.AlterField(
            model_name='student',
            name='last_name',
            field=models.CharField(max_length=100, verbose_name='nom'),
        ),
        migrations.AddField(
            model_name='student',
            name='classe',
            field=models.CharField(default='L1', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='phone',
            field=models.CharField(blank=True, max_length=20, verbose_name='téléphone'),
        ),
        migrations.AddField(
            model_name='student',
            name='birth_date',
            field=models.DateField(blank=True, null=True, verbose_name='date de naissance'),
        ),
        migrations.AddField(
            model_name='student',
            name='active',
            field=models.BooleanField(default=True, verbose_name='actif'),
        ),
        migrations.AddField(
            model_name='student',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
