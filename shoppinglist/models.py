from django.db import models
import datetime

# Create your models here.

class Shop(models.Model):
    name = models.CharField(max_length=100)
    shop_site = models.URLField(blank=True,null=True)

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=100)
    item_url = models.URLField(blank=True,null=True)
    count = models.PositiveIntegerField(default=0)
    buy_date = models.DateField(blank=True,null=True)
    shop = models.ForeignKey(Shop,blank=True,null=True,
                             verbose_name='shop', on_delete=models.PROTECT)
    buy = models.BooleanField(default=False)

    def __str__(self):
        return '{} ({})'.format(self.name, self.buy_date)

    def should_buy_today(self):
        """
        今日買うべきかを返す
        """
        today = datetime.date.today()
        buy_date = self.buy_date
        buy = self.buy

        # 期日が今日で、未購入であれば今日買うべき
        if buy_date == today and buy == False:
            return True
        else:
            return False