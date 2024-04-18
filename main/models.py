from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

class Book(models.Model):

    accsepted_list= [
        ('مقبول', 'مقبول'),
        ('مرفوض', 'مرفوض'),
        ('بانتظار', 'بانتظار')
    ]

    dat= models.DateField(verbose_name= 'تاريخ الحجز')
    tim= models.TimeField(verbose_name= 'وقت الحجز')
    num_of_hour= models.CharField(max_length=2, verbose_name= 'المدة', default='أدخل رقم الحجز، ساعتين على الأقل')
    phone= models.CharField(max_length= 100, verbose_name= 'موبايل', default= '+963 900 000 000')
    author = models.ForeignKey(
        get_user_model() ,
        on_delete = models.CASCADE,
        verbose_name= 'المستخدم'
    )
    name= models.CharField(max_length= 200, verbose_name= 'الاسم')
    notes= models.TextField(verbose_name= 'ملاحظات', null= True, blank= True)
    accsepted= models.CharField(max_length=50 , choices=accsepted_list ,
                                 null=True, blank=True, verbose_name= 'قبول الحجز',
                                   default= 'بانتظار')
    reson= models.TextField(verbose_name= 'ملاحظات من الأدمن', null= True, blank= True)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse('done')

