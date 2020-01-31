# Generated by Django 2.0.5 on 2019-12-31 17:45

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_operation', '0002_auto_20191231_1024'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraddress',
            name='city',
            field=models.CharField(default='', max_length=100, verbose_name='城市'),
        ),
        migrations.AddField(
            model_name='useraddress',
            name='province',
            field=models.CharField(default='', max_length=100, verbose_name='省份'),
        ),
        migrations.AlterField(
            model_name='userleavingmessage',
            name='file',
            field=models.FileField(help_text='上传的文件', upload_to='message/images/', verbose_name='上传的文件'),
        ),
        migrations.AlterUniqueTogether(
            name='userfav',
            unique_together={('user', 'goods')},
        ),
    ]
