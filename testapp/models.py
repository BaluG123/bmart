from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager
from django.urls import reverse

class CustomManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status="published")

# Create your models here
class Product(models.Model):
    status_choices=(('published','Published'),('draft','Draft'))
    company_choices=(('flifkart','FlipKart'),('amazon','Amazon'),('ajio','Ajio'),('myntra','Myntra'),('vcommission','vCommission'),('ebay','Ebay'),('hostgater','HostGator'),('admitad','Admitad'),('nearbuy','NearBuy'),('godaddy','GoDaddy'),('puma','Puma'))
    product_choices=(('fashion','Fashion'),('electronics','Electronics'),('others','Others'))
    product_name=models.CharField(max_length=64)
    slug=models.SlugField(max_length=64,unique_for_date="publish")
    name1=models.CharField(max_length=580,null=False,blank=False)
    image1=models.FileField(null=False,blank=False,upload_to='images/')
    link1=models.CharField(max_length=256,null=False,blank=False)
    detail1=models.TextField(null=False,blank=False)
    rprice1=models.IntegerField(null=False,blank=False)
    oprice1=models.IntegerField(null=False,blank=False)
    off1=models.IntegerField(null=False,blank=False)
    company1=models.CharField(max_length=64,choices=company_choices,default="amazon",null=False,blank=False)
    product1=models.CharField(max_length=64,choices=product_choices,default="fashion",null=False,blank=False)
    name2=models.CharField(max_length=580,null=True,blank=True)
    image2=models.FileField(null=True,blank=True,upload_to='images/')
    link2=models.CharField(max_length=256,null=True,blank=True)
    detail2=models.TextField(null=True,blank=True)
    rprice2=models.IntegerField(null=True,blank=True)
    oprice2=models.IntegerField(null=True,blank=True)
    off2=models.IntegerField(null=True,blank=True)
    company2=models.CharField(max_length=64,choices=company_choices,default="amazon",null=True,blank=True)
    product2=models.CharField(max_length=64,choices=product_choices,default="fashion",null=True,blank=True)
    name3=models.CharField(max_length=580,null=True,blank=True)
    image3=models.FileField(null=True,blank=True,upload_to='images/')
    link3=models.CharField(max_length=256,null=True,blank=True)
    detail3=models.TextField(null=True,blank=True)
    rprice3=models.IntegerField(null=True,blank=True)
    oprice3=models.IntegerField(null=True,blank=True)
    off3=models.IntegerField(null=True,blank=True)
    company3=models.CharField(max_length=64,choices=company_choices,default="amazon",null=True,blank=True)
    product3=models.CharField(max_length=64,choices=product_choices,default="fashion",null=True,blank=True)
    name4=models.CharField(max_length=500,null=True,blank=True)
    image4=models.FileField(null=True,blank=True,upload_to='images/')
    link4=models.CharField(max_length=256,null=True,blank=True)
    detail4=models.TextField(null=True,blank=True)
    rprice4=models.IntegerField(null=True,blank=True)
    oprice4=models.IntegerField(null=True,blank=True)
    off4=models.IntegerField(null=True,blank=True)
    company4=models.CharField(max_length=64,choices=company_choices,default="amazon",null=True,blank=True)
    product4=models.CharField(max_length=64,choices=product_choices,default="fashion",null=True,blank=True)
    publish=models.DateTimeField(default=timezone.now)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    objects=CustomManager()
    tags=TaggableManager()
    status=models.CharField(max_length=28,choices=status_choices,default='draft')

    class Meta:
        ordering=['-publish']

    def __str__(self):
        return self.product_name

    def get_absolute_url(self):
        return reverse('post_detail',args=[self.publish.year,self.publish.strftime('%m'),self.publish.strftime('%d'),self.slug])        