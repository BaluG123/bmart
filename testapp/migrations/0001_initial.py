# Generated by Django 3.2.3 on 2021-10-05 06:04

from django.db import migrations, models
import django.utils.timezone
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=64)),
                ('slug', models.SlugField(max_length=64, unique_for_date='publish')),
                ('name1', models.CharField(max_length=580)),
                ('image1', models.FileField(upload_to='images/')),
                ('link1', models.CharField(max_length=256)),
                ('detail1', models.TextField()),
                ('rprice1', models.IntegerField()),
                ('oprice1', models.IntegerField()),
                ('off1', models.IntegerField()),
                ('company1', models.CharField(choices=[('flifkart', 'FlipKart'), ('amazon', 'Amazon'), ('ajio', 'Ajio'), ('myntra', 'Myntra'), ('vcommission', 'vCommission'), ('ebay', 'Ebay'), ('hostgater', 'HostGator'), ('admitad', 'Admitad'), ('nearbuy', 'NearBuy'), ('godaddy', 'GoDaddy'), ('puma', 'Puma')], default='amazon', max_length=64)),
                ('product1', models.CharField(choices=[('fashion', 'Fashion'), ('electronics', 'Electronics'), ('others', 'Others')], default='fashion', max_length=64)),
                ('name2', models.CharField(blank=True, max_length=580, null=True)),
                ('image2', models.FileField(blank=True, null=True, upload_to='images/')),
                ('link2', models.CharField(blank=True, max_length=256, null=True)),
                ('detail2', models.TextField(blank=True, null=True)),
                ('rprice2', models.IntegerField(blank=True, null=True)),
                ('oprice2', models.IntegerField(blank=True, null=True)),
                ('off2', models.IntegerField(blank=True, null=True)),
                ('company2', models.CharField(blank=True, choices=[('flifkart', 'FlipKart'), ('amazon', 'Amazon'), ('ajio', 'Ajio'), ('myntra', 'Myntra'), ('vcommission', 'vCommission'), ('ebay', 'Ebay'), ('hostgater', 'HostGator'), ('admitad', 'Admitad'), ('nearbuy', 'NearBuy'), ('godaddy', 'GoDaddy'), ('puma', 'Puma')], default='amazon', max_length=64, null=True)),
                ('product2', models.CharField(blank=True, choices=[('fashion', 'Fashion'), ('electronics', 'Electronics'), ('others', 'Others')], default='fashion', max_length=64, null=True)),
                ('name3', models.CharField(blank=True, max_length=580, null=True)),
                ('image3', models.FileField(blank=True, null=True, upload_to='images/')),
                ('link3', models.CharField(blank=True, max_length=256, null=True)),
                ('detail3', models.TextField(blank=True, null=True)),
                ('rprice3', models.IntegerField(blank=True, null=True)),
                ('oprice3', models.IntegerField(blank=True, null=True)),
                ('off3', models.IntegerField(blank=True, null=True)),
                ('company3', models.CharField(blank=True, choices=[('flifkart', 'FlipKart'), ('amazon', 'Amazon'), ('ajio', 'Ajio'), ('myntra', 'Myntra'), ('vcommission', 'vCommission'), ('ebay', 'Ebay'), ('hostgater', 'HostGator'), ('admitad', 'Admitad'), ('nearbuy', 'NearBuy'), ('godaddy', 'GoDaddy'), ('puma', 'Puma')], default='amazon', max_length=64, null=True)),
                ('product3', models.CharField(blank=True, choices=[('fashion', 'Fashion'), ('electronics', 'Electronics'), ('others', 'Others')], default='fashion', max_length=64, null=True)),
                ('name4', models.CharField(blank=True, max_length=500, null=True)),
                ('image4', models.FileField(blank=True, null=True, upload_to='images/')),
                ('link4', models.CharField(blank=True, max_length=256, null=True)),
                ('detail4', models.TextField(blank=True, null=True)),
                ('rprice4', models.IntegerField(blank=True, null=True)),
                ('oprice4', models.IntegerField(blank=True, null=True)),
                ('off4', models.IntegerField(blank=True, null=True)),
                ('company4', models.CharField(blank=True, choices=[('flifkart', 'FlipKart'), ('amazon', 'Amazon'), ('ajio', 'Ajio'), ('myntra', 'Myntra'), ('vcommission', 'vCommission'), ('ebay', 'Ebay'), ('hostgater', 'HostGator'), ('admitad', 'Admitad'), ('nearbuy', 'NearBuy'), ('godaddy', 'GoDaddy'), ('puma', 'Puma')], default='amazon', max_length=64, null=True)),
                ('product4', models.CharField(blank=True, choices=[('fashion', 'Fashion'), ('electronics', 'Electronics'), ('others', 'Others')], default='fashion', max_length=64, null=True)),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('published', 'Published'), ('draft', 'Draft')], default='draft', max_length=28)),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'ordering': ['-publish'],
            },
        ),
    ]
