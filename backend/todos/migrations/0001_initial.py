# Generated by Django 3.2.9 on 2021-12-28 00:27

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('title', models.TextField()),
                ('description', models.TextField(blank=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('due_date', models.DateField(blank=True, null=True)),
                ('completed_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('description', models.TextField(blank=True)),
                ('topic', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['topic', 'title'],
            },
        ),
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('cost', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('img_url', models.URLField(blank=True, max_length=400)),
                ('product_url', models.URLField(blank=True, max_length=400)),
                ('count', models.IntegerField(default=0, null=True)),
                ('repeat', models.BooleanField(default=False)),
                ('last_purchased_date', models.DateField(blank=True, null=True)),
                ('tags', models.ManyToManyField(blank=True, to='todos.Tag')),
            ],
        ),
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('title', models.TextField()),
                ('description', models.TextField(blank=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('due_date', models.DateField(blank=True, null=True)),
                ('completed_date', models.DateField(blank=True, null=True)),
                ('frequency', models.CharField(blank=True, choices=[('DAILY', 'DAILY'), ('WEEKLY', 'WEEKLY'), ('MONTHLY', 'MONTHLY'), ('QUARTERLY', 'QUARTERLY'), ('YEARLY', 'YEARLY')], default=None, max_length=20, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('effort', models.DecimalField(decimal_places=2, default=0.5, max_digits=6)),
                ('reward', models.DecimalField(decimal_places=2, default=0.5, max_digits=6)),
                ('list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todos.list')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='list',
            name='tags',
            field=models.ManyToManyField(blank=True, to='todos.Tag'),
        ),
    ]
