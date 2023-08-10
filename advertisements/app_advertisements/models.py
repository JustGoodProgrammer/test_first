from django.db import models
from django.contrib import admin
from django.utils.html import format_html


class Advertisement(models.Model):
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
    


    def __str___(self):
        return f"Advertisement(id={self.id}, title={self.title}, price={self.price})"

    class Meta:
        db_table = 'advertisements'
