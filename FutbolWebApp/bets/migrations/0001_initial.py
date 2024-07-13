# Generated by Django 5.0.6 on 2024-07-05 16:03

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teamBets', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Bet',
                'verbose_name_plural': 'Bets',
                'db_table': 'bets',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='BetLine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('money_bet', models.IntegerField(default=1)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('bet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='betLines', to='bets.bet')),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teamBets.match')),
                ('team_bet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teamBets.team')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Bet Line',
                'verbose_name_plural': 'Bet Lines',
                'db_table': 'betLines',
                'ordering': ['id'],
            },
        ),
    ]
