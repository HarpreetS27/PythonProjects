# Generated by Django 3.2.3 on 2021-05-30 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShopSite', '0003_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('dborder_id', models.AutoField(primary_key=True, serialize=False)),
                ('dbitem_json', models.CharField(max_length=5000)),
                ('dbcust_name', models.CharField(max_length=200)),
                ('dbcust_email', models.CharField(max_length=200)),
                ('dbcust_adr', models.CharField(max_length=200)),
                ('dbcust_city', models.CharField(max_length=100)),
                ('dbcust_state', models.CharField(max_length=100)),
                ('dbcust_zip', models.IntegerField()),
                ('dbcust_phone', models.IntegerField()),
            ],
        ),
    ]
