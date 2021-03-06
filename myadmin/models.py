# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Article(models.Model):
    article_id = models.AutoField(primary_key=True)
    ud = models.ForeignKey('UserDetail', models.DO_NOTHING, blank=True, null=True)
    a_title = models.CharField(max_length=100)
    a_image = models.CharField(max_length=255, blank=True, null=True)
    view_num = models.IntegerField(blank=True, null=True)
    a_talk = models.IntegerField(blank=True, null=True)
    good_num = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'article'


class ArticleContent(models.Model):
    ac_id = models.AutoField(primary_key=True)
    article = models.ForeignKey(Article, models.DO_NOTHING, blank=True, null=True)
    content = models.TextField()

    class Meta:
        managed = False
        db_table = 'article_content'


class CityName(models.Model):
    city_id = models.AutoField(primary_key=True)
    vp = models.ForeignKey('ViewPlace', models.DO_NOTHING, blank=True, null=True)
    city_name = models.CharField(max_length=50, blank=True, null=True)
    city_img = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'city_name'


class EndProductRecommend(models.Model):
    bottom_id = models.AutoField(primary_key=True)
    vp = models.ForeignKey('Views', models.DO_NOTHING, blank=True, null=True)
    id = models.ForeignKey('EndRecommend', models.DO_NOTHING, db_column='id', blank=True, null=True)
    add_tell = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'end_product_recommend'


class EndRecommend(models.Model):
    recommend = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'end_recommend'


class HotPlay(models.Model):
    hi_id = models.AutoField(primary_key=True)
    v = models.ForeignKey('Views', models.DO_NOTHING, blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hot_play'


class LevelChange(models.Model):
    ch_l_id = models.AutoField(primary_key=True)
    ud = models.ForeignKey('UserDetail', models.DO_NOTHING, blank=True, null=True)
    b_level = models.IntegerField(blank=True, null=True)
    a_level = models.IntegerField(blank=True, null=True)
    ch_time = models.DateTimeField()
    ch_reson = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'level_change'


class MemberLevelDesc(models.Model):
    mem_l_id = models.AutoField(primary_key=True)
    ud = models.ForeignKey('UserDetail', models.DO_NOTHING, blank=True, null=True)
    mem_l_detail = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'member_level_desc'


class OrderDiscuss(models.Model):
    od_id = models.AutoField(primary_key=True)
    ud = models.ForeignKey('UserDetail', models.DO_NOTHING, blank=True, null=True)
    order = models.ForeignKey('OrderTable', models.DO_NOTHING, blank=True, null=True)
    stars = models.IntegerField(blank=True, null=True)
    content = models.CharField(max_length=255, blank=True, null=True)
    is_public = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_discuss'


class OrderTable(models.Model):
    order_id = models.AutoField(primary_key=True)
    v = models.ForeignKey('Views', models.DO_NOTHING, blank=True, null=True)
    ud = models.ForeignKey('UserDetail', models.DO_NOTHING, blank=True, null=True)
    get_time = models.DateTimeField(blank=True, null=True)
    pay_time = models.DateTimeField(blank=True, null=True)
    last_time = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    no_need = models.DateTimeField(blank=True, null=True)
    return_money_time = models.DateTimeField(blank=True, null=True)
    is_talk = models.IntegerField(blank=True, null=True)
    order_name = models.CharField(max_length=50, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    start_time = models.DateField(blank=True, null=True)
    order_type = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_table'


class ProductRecommend(models.Model):
    discount = models.ForeignKey('WedDiscount', models.DO_NOTHING, blank=True, null=True)
    v = models.ForeignKey('Views', models.DO_NOTHING, blank=True, null=True)
    inventory = models.IntegerField(blank=True, null=True)
    discount_price = models.FloatField(blank=True, null=True)
    limit_cnt = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_recommend'


class Record(models.Model):
    record_id = models.AutoField(primary_key=True)
    ud = models.ForeignKey('UserDetail', models.DO_NOTHING, blank=True, null=True)
    record_name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'record'


class ScoreSave(models.Model):
    score_save_id = models.AutoField(primary_key=True)
    ud = models.ForeignKey('UserDetail', models.DO_NOTHING, blank=True, null=True)
    num = models.IntegerField(blank=True, null=True)
    get_record = models.CharField(max_length=50, blank=True, null=True)
    get_time = models.DateField(blank=True, null=True)
    get_way = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'score_save'


class SysInfo(models.Model):
    sys_info_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    info = models.CharField(max_length=255, blank=True, null=True)
    info_detail = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_info'


class SysRole(models.Model):
    name = models.CharField(unique=True, max_length=50)
    code = models.CharField(unique=True, max_length=20)

    class Meta:
        managed = False
        db_table = 'sys_role'


class SysTicket(models.Model):
    sys_ticket_id = models.AutoField(primary_key=True)
    st_name = models.CharField(max_length=20)
    st_money = models.FloatField()
    st_ticket_desc = models.CharField(max_length=200, blank=True, null=True)
    is_use = models.IntegerField(blank=True, null=True)
    st_tiaojian = models.CharField(max_length=20, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_ticket'


class SysUser(models.Model):
    name = models.CharField(unique=True, max_length=50)
    auth_string = models.CharField(max_length=100)
    email = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return "%s %s %s %s" % (self.name, self.auth_string, self.email, self.phone)

    @property
    def role(self):
        role_id = SysUserRole.objects.get(user_id=self.id).role_id
        return SysRole.objects.get(pk=role_id)

    class Meta:
        managed = False
        db_table = 'sys_user'


class SysUserRole(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    role_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_user_role'


class TravelCircle(models.Model):
    tr_id = models.AutoField(primary_key=True)
    vp = models.ForeignKey('Views', models.DO_NOTHING, blank=True, null=True)
    head_picture = models.CharField(max_length=200, blank=True, null=True)
    nickname = models.CharField(max_length=20, blank=True, null=True)
    pic_dis = models.CharField(max_length=200, blank=True, null=True)
    sign = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'travel_circle'


class TravelLife(models.Model):
    tf_id = models.AutoField(primary_key=True)
    picture = models.CharField(max_length=200, blank=True, null=True)
    pic_dis = models.CharField(max_length=50, blank=True, null=True)
    tip = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'travel_life'


class TravelerInfo(models.Model):
    travel_id = models.AutoField(primary_key=True)
    ud = models.ForeignKey('UserDetail', models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    gender = models.IntegerField(blank=True, null=True)
    id_card = models.IntegerField(blank=True, null=True)
    phone_num = models.CharField(max_length=20, blank=True, null=True)
    go_date = models.DateTimeField(blank=True, null=True)
    p_type = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'traveler_info'


class UserAccount(models.Model):
    user_id = models.AutoField(primary_key=True)
    ud = models.ForeignKey('UserDetail', models.DO_NOTHING, blank=True, null=True)
    user_name = models.CharField(max_length=20, blank=True, null=True)
    user_password = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_account'


class UserDetail(models.Model):
    ud_id = models.AutoField(primary_key=True)
    nick_name = models.CharField(max_length=25, blank=True, null=True)
    real_name = models.CharField(max_length=20, blank=True, null=True)
    ud_gender = models.IntegerField(blank=True, null=True)
    ud_email = models.CharField(max_length=50, blank=True, null=True)
    ud_img = models.TextField(blank=True, null=True)
    ud_job = models.CharField(max_length=20, blank=True, null=True)
    ud_level = models.CharField(max_length=200, blank=True, null=True)
    ud_info = models.CharField(max_length=200, blank=True, null=True)
    adress = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_detail'


class UserTicket(models.Model):
    user_ticket_id = models.AutoField(primary_key=True)
    ud = models.ForeignKey(UserDetail, models.DO_NOTHING, blank=True, null=True)
    sys_ticket = models.ForeignKey(SysTicket, models.DO_NOTHING, blank=True, null=True)
    ut_desc = models.CharField(max_length=200, blank=True, null=True)
    is_use = models.IntegerField(blank=True, null=True)
    ut_tiaojian = models.CharField(max_length=50, blank=True, null=True)
    ut_money = models.FloatField(blank=True, null=True)
    ut_name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_ticket'


class UserWallet(models.Model):
    wallet_id = models.AutoField(primary_key=True)
    ud = models.ForeignKey(UserDetail, models.DO_NOTHING, blank=True, null=True)
    w_acount = models.FloatField(blank=True, null=True)
    rest_money = models.FloatField(blank=True, null=True)
    recharge = models.FloatField(blank=True, null=True)
    is_have = models.IntegerField(blank=True, null=True)
    is_display = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_wallet'


class ViewPlace(models.Model):
    vp_id = models.IntegerField(primary_key=True)
    city_name = models.CharField(max_length=10)
    province_name = models.CharField(max_length=10)
    district_name = models.CharField(max_length=10)
    city_img = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'view_place'


class Views(models.Model):
    v_id = models.AutoField(primary_key=True)
    city = models.ForeignKey(CityName, models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    v_desc = models.CharField(max_length=255, blank=True, null=True)
    v_pic = models.CharField(max_length=200, blank=True, null=True)
    v_route = models.CharField(max_length=500, blank=True, null=True)
    is_youhui = models.IntegerField(blank=True, null=True)
    is_special = models.IntegerField(blank=True, null=True)
    travel_way = models.CharField(max_length=10, blank=True, null=True)
    diamonds = models.CharField(max_length=10, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    start_time = models.DateField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    count_num = models.IntegerField(blank=True, null=True)
    cost_days = models.IntegerField(blank=True, null=True)
    reason = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'views'


class WedDiscount(models.Model):
    dis_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wed_discount'


class WheelTable(models.Model):
    wheel_id = models.AutoField(primary_key=True)
    img_url = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wheel_table'
