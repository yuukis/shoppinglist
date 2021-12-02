from django.test import TestCase
import datetime

# Create your tests here.
from .models import Item

class ItemModelTests(TestCase):
    def test_should_buy_today1(self):
        """
        メロンは今日期日で未購入のため、今日買うべき
        """
        today = datetime.date.today()
        item = Item()
        item.name = 'メロン'
        item.count = 1
        item.buy_date = today
        item.buy = False
        self.assertIs(item.should_buy_today(), True)

    def test_should_buy_today2(self):
        """
        ブドウは明日期日のため、今日買う必要は無い
        """
        tomorrow = datetime.date.today() + datetime.timedelta(days=1)
        item = Item()
        item.name = 'ブドウ'
        item.count = 2
        item.buy_date = tomorrow
        item.buy = False
        self.assertIs(item.should_buy_today(), False)

    def test_should_buy_today3(self):
        """
        ミカンは購入済みのため、今日買う必要は無い
        """
        today = datetime.date.today()
        item = Item()
        item.name = 'ミカン'
        item.count = 3
        item.buy_date = today
        item.buy = True
        self.assertIs(item.should_buy_today(), False)