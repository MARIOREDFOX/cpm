# Generated by Django 4.0.3 on 2022-03-20 11:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Minority',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='NewsLetter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='One',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='OrganisationCpm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Qualification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='SocioCultureCaste',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.DateField(blank=True, null=True)),
                ('period_of_joining', models.DateField(blank=True, null=True)),
                ('income', models.IntegerField(default=1)),
                ('levy_cash', models.IntegerField(default=1)),
                ('disabled', models.BooleanField(default=False)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='members.category')),
                ('classes', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='members.classes')),
                ('gender', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='members.gender')),
                ('minority', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='members.minority')),
                ('news_letter', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='members.newsletter')),
                ('one', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='members.one')),
                ('organisation_cpm', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='members.organisationcpm')),
                ('qualification', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='members.qualification')),
                ('socio_culture_caste', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='members.socioculturecaste')),
            ],
        ),
    ]
