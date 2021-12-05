from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import (post_save)
from django.core.mail import send_mail

# Create your models here.


class Question(models.Model):
    question = models.CharField(max_length=1000, blank=False, default='')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user', on_delete=models.CASCADE)
    mentor = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='mentor', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'questions'



class Answer(models.Model):
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=2000, blank=False)

    class Meta:
        verbose_name_plural = 'answers'


@receiver(post_save, sender=Question)
def question_created_handler(sender, instance, created, *args, **kwargs):
    if created:
        print("send email to", instance.mentor.email)
        send_mail(f'Askme, Hi {instance.mentor} we have a question for you?', f'instance.question /n You can reply to this question on Askme app', instance.user,
                  [instance.mentor.email])
    print("Hi", args, kwargs)
