from django.db import models


class Account(models.Model):
    billingpostalcode = models.CharField(max_length=20, null=True, blank=True)
    isdeleted = models.BooleanField(default=False)
    id = models.IntegerField(primary_key=True, unique=True)
    billinglatitude = models.DecimalField(
        max_digits=11,
        decimal_places=8,
        null=True,
        blank=True)
    _hc_lastop = models.CharField(max_length=32, null=True, blank=True)
    createddate = models.DateTimeField(null=True, blank=True)
    billingcountry = models.CharField(max_length=80, null=True, blank=True)
    geolocation_longitude_s = models.DecimalField(
        max_digits=11,
        decimal_places=8,
        db_column='geolocation__longitude__s',
        null=True,
        blank=True)
    geolocation_latitude_s = models.DecimalField(
        max_digits=11,
        decimal_places=8,
        db_column='geolocation__latitude__s',
        null=True,
        blank=True)
    billingstate = models.CharField(max_length=80, null=True, blank=True)
    billingstreet = models.CharField(max_length=255, null=True, blank=True)
    billinglongitude = models.DecimalField(
        max_digits=11,
        decimal_places=8,
        null=True,
        blank=True)
    billingcity = models.CharField(max_length=40, null=True, blank=True)
    systemmodstamp = models.DateTimeField(null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    _hc_err = models.TextField(null=True, blank=True, max_length=1024)
    sfid = models.CharField(max_length=18, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'salesforce\".\"account'
        verbose_name = 'Salesforce Account'
        verbose_name_plural = 'Salesforce Accounts'


class AccountAddon(models.Model):
    account = models.OneToOneField(Account,
                                   related_name='accountaddons',
                                   on_delete=models.CASCADE)
    schedule = models.CharField(max_length=200, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_featured = models.BooleanField(default=False)
    avg_consumer_spending = models.IntegerField(null=True, blank=True)
    menu_best_sellers = models.TextField(null=True, blank=True)
    author = models.ForeignKey('myuser.MyUser', null=True, blank=True)
    last_update_datetime = models.DateTimeField(null=True, blank=True)
    category = models.CharField(max_length=50, null=True, blank=True)
    is_type = models.CharField(default='Account', max_length=50)

    def __str__(self):
        return str(self.account)

    class Meta:
        verbose_name_plural = 'Account Addons'
        db_table = 'cms_account_addon'