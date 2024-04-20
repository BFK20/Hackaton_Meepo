# Generated by Django 4.2.11 on 2024-04-20 12:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lifecourse', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vuses',
            old_name='vusname',
            new_name='name',
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lifecourse.department')),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lifecourse.faculty')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lifecourse.group')),
                ('university', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lifecourse.vuses')),
            ],
        ),
    ]
