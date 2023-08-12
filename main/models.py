from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Students(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    avatar = models.ImageField(upload_to='students/', verbose_name='Аватар', **NULLABLE)

    email = models.CharField(max_length=150, verbose_name='email', unique=True, **NULLABLE)

    is_active = models.BooleanField(default=True, verbose_name='учится')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'студент'
        verbose_name_plural = 'студенты'
        ordering = ('last_name',)


class Subject(models.Model):
    title = models.CharField(max_length=150, verbose_name='название')
    discription = models.TextField(verbose_name='описание')

    student = models.ForeignKey(Students, on_delete=models.CASCADE, verbose_name='студент')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'предмет'
        verbose_name_plural = 'предметы'
