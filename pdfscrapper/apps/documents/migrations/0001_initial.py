from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=(
                ('id', models.AutoField(auto_created=True, primary_key=True,
                                        serialize=False, verbose_name='ID')),
                ('name', models.CharField(null=False, max_length=500,
                                          verbose_name='Name'))
            ),
            options={
                'verbose_name': 'Document',
                'verbose_name_plural': 'Documents',
                'db_table': 'documents',
                'managed': True
            }
        ),
        migrations.CreateModel(
            name='URL',
            fields=(
                ('id', models.AutoField(auto_created=True, primary_key=True,
                                        serialize=False, verbose_name='ID')),
                ('link', models.URLField(null=False, max_length=500,
                                         verbose_name='Link')),
                ('active', models.BooleanField(verbose_name='Active')),
                ('document', models.ForeignKey(
                    on_delete=models.deletion.CASCADE, related_name='links',
                    related_query_name='links', to='Document',
                    verbose_name='Document'))
            ),
            options={
                'verbose_name': 'Link',
                'verbose_name_plural': 'Links',
                'db_table': 'links',
                'managed': True
            }
        )
    ]
