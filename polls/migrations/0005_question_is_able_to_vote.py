# Generated by Django 4.2.5 on 2023-09-07 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_alter_question_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='is_able_to_vote',
            field=models.BooleanField(default=True),
        ),
    ]
