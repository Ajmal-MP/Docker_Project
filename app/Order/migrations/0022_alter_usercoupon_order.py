# Generated by Django 4.1 on 2022-10-03 21:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0021_alter_usercoupon_total_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercoupon',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order_coupon', to='Order.order'),
        ),
    ]
