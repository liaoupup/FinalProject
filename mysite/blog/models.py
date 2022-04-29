from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.contenttypes.models import ContentType
from read_statistics.models import ReadNumExpandMethod, ReadDetail
from django.contrib.contenttypes.fields import GenericRelation

class Motto(models.Model):
    content = RichTextUploadingField()


class Blog(models.Model, ReadNumExpandMethod):
    title = models.CharField(max_length=30)
    content = RichTextUploadingField()
    read_details = GenericRelation(ReadDetail)
    blog_type = models.ForeignKey('BlogType',
                                  on_delete=models.DO_NOTHING)  # 外键-博客类型-一对一,如果你需要在一个尚未定义的模型上创建关系，你可以使用模型的名称，而不是模型对象本身
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)  # 外键
    created_time = models.DateTimeField(auto_now_add=True)
    last_updated_time = models.DateTimeField(auto_now=True)



    def __str__(self):
        return "<Blog: %s>" % self.title

    class Meta:
        ordering = ['-created_time']


class BlogType(models.Model):
    type_name = models.CharField(max_length=15)

    def __str__(self):
        return self.type_name


# class ReadNum(models.Model):
#     read_num = models.IntegerField(default=0)
#     blog = models.OneToOneField(Blog, on_delete=models.DO_NOTHING)
