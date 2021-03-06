# Generated by Django 2.0.5 on 2020-01-02 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0002_auto_20191231_1024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderinfo',
            name='pay_status',
            field=models.CharField(choices=[('success', '成功'), ('cancel', '取消'), ('paying', '待支付')], default='paying', max_length=30, verbose_name='订单状态'),
        ),
    ]
