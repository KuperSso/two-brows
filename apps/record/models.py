import uuid
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
  

class Services(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    title = models.CharField(max_length=255, verbose_name="Название услуги")
    description = models.TextField(verbose_name="Описание услуги")
    photo = models.ImageField(upload_to="photos/cards/%Y/%m/%d/", blank=True)
    time_created = models.DateTimeField(auto_now_add=True)

  

    class Meta:
        db_table = "services_main"
        verbose_name = "Услугу"
        verbose_name_plural = "Услуги"
        ordering = ["time_created"]

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("record_detail", kwargs={"pk":str(self.id)})

  

class Record (models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    service = models.ForeignKey(
        Services ,
        on_delete=models.CASCADE,
        null=True,
        related_name="service",
        verbose_name="Выбранная услуга"
    )

    patient = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        null=True,
        related_name="user",
        verbose_name="Пациент"
    )
    date_time = models.DateTimeField(verbose_name="Выбирете дату и время")
    approved = models.BooleanField(blank=True, default=False, verbose_name="Одобрить")

    class Meta:
        db_table = "records_main"
        verbose_name = "Запись"
        verbose_name_plural = "Записи"
        ordering = ["date_time"]

    def __str__(self):
        return self.service.title