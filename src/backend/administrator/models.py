from django.db import models

# Create your models here.


class Administrator(models.Model):
    admin_name = models.CharField(primary_key=True, max_length=20, default='')
    admin_password = models.CharField(max_length=20, default='')
    power_create_camp = models.BooleanField(default=False)
    power_create_course = models.BooleanField(default=False)
    power_create_activity = models.BooleanField(default=False)
    power_create_administrator = models.BooleanField(default=False)


class Campclass(models.Model):
    name = models.CharField(max_length=20)  # 班级名字
    student_number = models.IntegerField(default=0)  # 班级人数
    camp_id = models.IntegerField()


class Camp(models.Model):
    name = models.CharField(max_length=20)
    time = models.CharField(max_length=40)
    introduce = models.TextField()
    people_oriented = models.TextField()  # 面向人群
    signin_tips = models.TextField()
    signin_deadline = models.CharField(max_length=100)
    permission = models.IntegerField(default=0)


class Course(models.Model):
    name = models.CharField(max_length=20)
    time = models.CharField(max_length=40)
    location = models.CharField(max_length=40)
    teacher = models.CharField(max_length=40)
    abstract = models.TextField()  # 梗概
    belongto_camp = models.CharField(max_length=40)
    belongto_campclass = models.CharField(max_length=40)
    number_bystander = models.IntegerField(default=0)
    bystand_tips = models.TextField()


class Coursebystander(models.Model):
    user_id = models.IntegerField()
    course_id = models.IntegerField()


class Campsignup(models.Model):
    user_id = models.IntegerField()
    camp_id = models.IntegerField()
    campclass_id = models.IntegerField(default=0)


class Campattend(models.Model):
    user_id = models.IntegerField()
    camp_id = models.IntegerField()


class User(models.Model):
    GENDER_CHIOCES = (
        ('m', '男'),
        ('f', '女'),
    )
    user_name = models.CharField(max_length=20)
    user_gender = models.CharField(max_length=1, choices=GENDER_CHIOCES)
    user_weixinnumber = models.CharField(max_length=20)  # 微信号
    user_telephone = models.CharField(max_length=11)  # 电话
    user_email = models.EmailField()  # 邮箱


class Userdata(models.Model):
    POST_LIST = (
        ('F', '创始人'),
        ('CF', '联合创始人'),
        ('P', '董事长'),
        ('CEO', 'CEO'),
        ('Others', '其他'),
    )
    EDUCATED_LIST = (
        ('PhD', '博士研究生'),
        ('MBA', '硕士研究生'),
        ('Bachelor', '本科'),
        ('College', '专科'),
        ('Others', '其他'),
    )
    WAY_TO_CAMP = (
        ('weixin', '微信朋友圈'),
        ('friend', '朋友推荐'),
        ('Pubaccount', '未来之星公众号：EdStars未来同学会'),
        ('web', '好未来官网'),
        ('media', '媒体报道'),
        ('others', '其他'),
    )
    user_id = models.IntegerField()
    user_birthday = models.CharField(max_length=30)  # 用户出生日期
    user_company = models.IntegerField()  # 公司id
    user_post = models.CharField(max_length=30, choices=POST_LIST)  # 职务
    user_city = models.CharField(max_length=10)  # 用户所在城市
    user_referee1_message = models.TextField(blank=False)  # 推荐人信息
    user_referee2_message = models.TextField()
    user_referee3_message = models.TextField()
    user_other_tips_message_question_for_absenceitem = models.CharField(
        max_length=4)  # 认可与否缺勤制度
    reasons_for_signin = models.TextField()  # 加入理由
    contribution_to_others = models.TextField()  # 能为其他人带来什么
    messageway_to_camp = models.CharField(
        max_length=20, choices=WAY_TO_CAMP)
    educated_condition = models.CharField(
        max_length=10, choices=EDUCATED_LIST)  # 用户受教育程度
    user_educondition_time_detials = models.TextField()  # 用户最高学历时间情况
    user_beforestartup_company_condition = models.TextField()  # 用户创业前的从业情况


class Usercompany(models.Model):
    FINANCING_SITUATION = (
        ('N', '尚未获得融资'),
        ('seed/angel', '已完成种子/天使融资'),
        ('pre-A', '已完成pre-A轮融资'),
        ('A', '已完成A轮融资'),
        ('refuse', '不方便透露'),
        ('others', '其他'),
    )
    name = models.CharField(max_length=40, default='')
    brand_name = models.CharField(
        default='无', max_length=40)  # 公司品牌
    website = models.CharField(default='无', max_length=50)  # 公司网站
    app_or_publicAccounts = models.CharField(
        default='无', max_length=20)  # 公司应用或公众号
    startup_time = models.CharField(max_length=30)  # 公司成立时间
    center_city = models.CharField(max_length=10)  # 公司总部所在城市
    membership = models.IntegerField(default=0)  # 公司人员数量
    abstract = models.TextField()  # 公司/项目介绍
    main_operational_data = models.TextField()  # 主要运营数据
    income_scale = models.CharField(max_length=20)  # 收入规模
    financing_situation = models.CharField(
        max_length=15, choices=FINANCING_SITUATION)  # 融资情况
    value_of_assessment = models.CharField(max_length=20, default='')  # 市场估值
    additions = models.TextField(default='')  # 公司补充说明


class Activity(models.Model):
    STATUS_LIST = (
        ('N', 'NotStart'),
        ('O', 'Ongoing'),
        ('F', 'Finished'),
    )
    activity_name = models.CharField(max_length=20)
    activity_time = models.CharField(max_length=200)
    activity_location = models.CharField(max_length=30)
    activity_abstract = models.TextField()
    activity_peopleneed = models.IntegerField(default=0)  # 活动大体需要人数
    activity_tips = models.TextField()  # 活动注意事项
    activity_status = models.CharField(
        max_length=1, choices=STATUS_LIST)  # 活动目前状态
    activity_items = models.TextField(default='')  # 活动具体流程


class Activitytakes(models.Model):
    attender_id = models.IntegerField()
    activity_id = models.IntegerField()


class Coursefile(models.Model):
    course_id = models.IntegerField(default=0)
    ppt_name = models.CharField(max_length=100, default='', blank=True)
    ppt = models.FileField(upload_to='ppt', blank=True)
    video_name = models.CharField(max_length=100, default='', blank=True)
    video = models.FileField(upload_to='video', blank=True)
    text_name = models.CharField(max_length=100, default='', blank=True)
    text = models.FileField(upload_to='text', blank=True)
    others_name = models.CharField(max_length=100, default='', blank=True)
    others = models.FileField(upload_to='othersFile', blank=True)
