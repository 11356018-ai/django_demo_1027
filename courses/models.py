from django.conf import settings
from django.db import models


class Course(models.Model):
    STATUS_PENDING = 'pending'
    STATUS_APPROVED = 'approved'
    STATUS_REJECTED = 'rejected'

    STATUS_CHOICES = [
        (STATUS_PENDING, '待審核'),
        (STATUS_APPROVED, '已核准'),
        (STATUS_REJECTED, '已退回'),
    ]

    code = models.CharField('課程代碼', max_length=20)
    name = models.CharField('課程名稱', max_length=200)
    credits = models.PositiveIntegerField('學分')
    instructor = models.CharField('授課老師', max_length=100, blank=True)
    location = models.CharField('上課地點', max_length=100, blank=True)
    schedule = models.CharField('上課時間', max_length=200, blank=True)
    capacity = models.PositiveIntegerField('課程容量', default=40)
    description = models.TextField('課程簡介', blank=True)
    proposer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='proposed_courses',
        verbose_name='提案人',
    )
    status = models.CharField(
        '審核狀態',
        max_length=10,
        choices=STATUS_CHOICES,
        default=STATUS_PENDING,
    )
    created_at = models.DateTimeField('建立時間', auto_now_add=True)
    updated_at = models.DateTimeField('更新時間', auto_now=True)

    class Meta:
        ordering = ['code']
        verbose_name = '課程'
        verbose_name_plural = '課程'

    def __str__(self):
        return f'{self.code} - {self.name}'

    @property
    def enrolled_count(self):
        return self.enrollments.count()

    @property
    def is_full(self):
        return self.enrolled_count >= self.capacity


class Enrollment(models.Model):
    student = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='enrollments',
        verbose_name='學生',
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='enrollments',
        verbose_name='課程',
    )
    enrolled_at = models.DateTimeField('加選時間', auto_now_add=True)

    class Meta:
        unique_together = [['student', 'course']]
        ordering = ['enrolled_at']
        verbose_name = '選課紀錄'
        verbose_name_plural = '選課紀錄'

    def __str__(self):
        return f'{self.student} -> {self.course}'
