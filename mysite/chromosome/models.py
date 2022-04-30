from django.db import models
from django.contrib.auth.models import User
from read_statistics.models import ReadNumExpandMethod, ReadDetail
from django.contrib.contenttypes.fields import GenericRelation

class Abnormal(models.Model, ReadNumExpandMethod):
    CHROMOSOME_CHOICES = [
        ('1', '1号染色体'),
        ('2', '2号染色体'),
        ('3', '3号染色体'),
        ('4', '4号染色体'),
        ('5', '5号染色体'),
        ('6', '6号染色体'),
        ('7', '7号染色体'),
        ('8', '8号染色体'),
        ('9', '9号染色体'),
        ('10', '10号染色体'),
        ('11', '11号染色体'),
        ('12', '12号染色体'),
        ('13', '13号染色体'),
        ('14', '14号染色体'),
        ('15', '15号染色体'),
        ('16', '16号染色体'),
        ('17', '17号染色体'),
        ('18', '18号染色体'),
        ('19', '19号染色体'),
        ('20', '20号染色体'),
        ('21', '21号染色体'),
        ('22', '22号染色体'),
        ('X', 'X染色体'),
        ('Y', 'Y染色体'),

    ]
    read_details = GenericRelation(ReadDetail)
    description = models.CharField("表型", max_length=100, help_text="表型/临床指征")
    karyotype = models.CharField("核型描述", max_length=30, help_text="遵循ISCN2020描述的核型输入")
    broken_site = models.CharField("断裂点位", max_length=30, help_text="断裂点位（可选）", null=True, blank=True)
    fragile_site = models.CharField("脆性位点", max_length=30, help_text="脆性位点（可选）", null=True, blank=True)
    abnormal_type = models.ManyToManyField('AbnormalType', related_name='abnormal')
    chromosome = models.CharField("涉及染色体", max_length=2, help_text="涉及染色体", choices=CHROMOSOME_CHOICES)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    image = models.ImageField(upload_to='images/', null=True, blank=True, help_text="建议核型图片数量在10张以内，支持 jpg/jpeg、png、bmp、tif 等图片格式")
    created_time = models.DateTimeField(auto_now_add=True)
    last_updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "<Abnormal: %s>" % self.karyotype

    class Meta:
        ordering = ['-created_time']

class Reference(models.Model):
    abnormal = models.OneToOneField(Abnormal, null=True, on_delete=models.CASCADE, related_name='reference')
    pmid = models.IntegerField('PMID', help_text='PubMed唯一标识码')
    title = models.CharField('标题', max_length=40, help_text='请输入标题')
    abstract = models.TextField('摘要', help_text='请输入摘要')
    pdf = models.FileField(upload_to='pdfs/')

    def __str__(self):
        return self.title

class AbnormalType(models.Model):
    name = models.CharField('异常类型', max_length=10)
    created_time = models.DateTimeField(auto_now_add=True)
    last_updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


