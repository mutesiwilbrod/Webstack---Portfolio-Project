# Generated by Django 5.0.6 on 2024-07-22 06:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('miu', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='application',
            old_name='cet_scorecard',
            new_name='uace_leaving_certificate',
        ),
        migrations.RenameField(
            model_name='application',
            old_name='hsc_percentage',
            new_name='uace_points',
        ),
        migrations.RenameField(
            model_name='application',
            old_name='ssc_percentage',
            new_name='uce_aggregates',
        ),
        migrations.RenameField(
            model_name='application',
            old_name='hsc_leaving_certificate',
            new_name='uce_certificate',
        ),
        migrations.RemoveField(
            model_name='application',
            name='cet_percentile',
        ),
        migrations.RemoveField(
            model_name='application',
            name='hsc_marksheet',
        ),
        migrations.RemoveField(
            model_name='application',
            name='hsc_passing_certificate',
        ),
        migrations.RemoveField(
            model_name='application',
            name='jee_percentile',
        ),
        migrations.RemoveField(
            model_name='application',
            name='jee_scorecard',
        ),
        migrations.RemoveField(
            model_name='application',
            name='ssc_leaving_certificate',
        ),
        migrations.RemoveField(
            model_name='application',
            name='ssc_marksheet',
        ),
        migrations.RemoveField(
            model_name='application',
            name='ssc_passing_certificate',
        ),
    ]