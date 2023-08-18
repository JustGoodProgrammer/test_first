from django.db import models
from django.contrib import admin
from django.utils.html import format_html
from django.contrib.auth import get_user_model


User = get_user_model()


class Advertisement(models.Model):

    user = models.ForeignKey(
        User,
        verbose_name='пользователь',
        on_delete=models.CASCADE
    )

    image = models.ImageField(
        'Изображение',
        upload_to='advertisments/'
    )

    # Товар
    # строковое поле для небольших размеров
    # 'заголовок' - verbose_name - название поля извне
    title = models.CharField('заголовок', max_length=128)

    # Описание товара/информация о товаре
    # Большое текстовое поле, для больших текстов
    description = models.TextField('описание')

    # Цена
    # Специальный тип данных с фиксированной точкой
    price = models.DecimalField('цена', max_digits=10, decimal_places=2)

    # Уместен ли торг
    # Логический тип, два значения - правда или ложь
    auction = models.BooleanField('Уместен ли торг?', help_text = 'Можно ли с вами торговаться?')

    # Дата публикации
    # Поле записывается при создании объявления
    created_at = models.DateTimeField(auto_now_add=True)

    # Дата изменения/обновления
    # Поле записывается при каждом обновлении
    updated_at = models.DateTimeField(auto_now=True)

    @admin.display(description='Дата создания')
    def created_date(self):
        from django.utils import timezone
        if self.created_at.date() == timezone.now().date():
            created_date = self.created_at.strftime("%H:%M:%S")
            return format_html('<spam style="color:green; font weight:bold;"> Сегодня в {} </spam>', created_date)
        else:
            return self.created_at.strftime("%d.%m.%Y в %H:%M:%S")
    
    @admin.display(description='Дата обновления')
    def updated_date(self):
        from django.utils import timezone
        if self.updated_at.date() == timezone.now().date():
            updated_date = self.updated_at.strftime("%H:%M:%S")
            return format_html('<spam style="color:blue; font weight:bold;"> Сегодня в {} </spam>', updated_date)
        else:
            return self.updated_at.strftime("%d.%m.%Y в %H:%M:%S")

    @admin.display(description='Фото')
    def get_html_image(self):
        if self.image:
            return format_html(
                '<img src="{}" style="max-width:80px; max-height:80px"></img>',
                self.image.url
            )

    def __str___(self):
        return f"Advertisement(id={self.id}, title={self.title}, price={self.price})"

    class Meta:
        db_table = 'advertisements'
