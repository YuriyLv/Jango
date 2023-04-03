from django.db import models
import markdown

class Category(models.Model):
    category_name = models.CharField('category_name', max_length=30)
    def __str__(self):
        return f'{self.category_name}'

class Post(models.Model):
    index = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='category', null=True, blank=True)
    title = models.CharField('title_field', max_length=100)
    description = models.TextField('text_field')
    author = models.CharField('author_name_field', max_length=100)
    data = models.DateField('data_field')
    def description_as_html(self):
        return markdown.markdown(self.description)
    def __str__(self):
        return f'{self.index}, {self.title}, {self.data}'
