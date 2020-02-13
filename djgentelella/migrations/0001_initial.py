# Generated by Django 3.0.2 on 2020-02-13 13:39

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='GentelellaSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=100)),
                ('value', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.SlugField(unique=True)),
                ('title', models.CharField(max_length=500)),
                ('url_name', models.CharField(max_length=500)),
                ('category', models.CharField(default='main', help_text='Clasifica items', max_length=200)),
                ('is_reversed', models.BooleanField(default=False)),
                ('reversed_kwargs', models.CharField(blank=True, max_length=500, null=True)),
                ('reversed_args', models.CharField(blank=True, max_length=500, null=True)),
                ('is_widget', models.BooleanField(default=False)),
                ('icon', models.CharField(blank=True, max_length=50, null=True)),
                ('only_icon', models.BooleanField(default=False)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='djgentelella.MenuItem')),
                ('permission', models.ManyToManyField(blank=True, to='auth.Permission')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]