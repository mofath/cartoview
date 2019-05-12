# Generated by Django 2.2 on 2019-05-02 12:03

from django.db import migrations, models
import wagtail.contrib.table_block.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('additional_info', models.TextField(blank=True, null=True)),
                ('upload_file', models.FileField(blank=True, null=True, upload_to='')),
                ('values', wagtail.core.fields.StreamField([('table', wagtail.contrib.table_block.blocks.TableBlock())])),
            ],
            options={
                'verbose_name': 'Data Table',
                'verbose_name_plural': 'Data Tables',
            },
        ),
    ]