# Generated by Django 2.1.5 on 2019-03-22 16:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('memberaccount', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member_shares',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('document_no', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=200)),
                ('debit_amount', models.CharField(max_length=200)),
                ('credit_amount', models.CharField(max_length=200)),
                ('balance', models.CharField(max_length=200)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('approved_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]