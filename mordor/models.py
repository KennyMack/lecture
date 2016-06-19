from django.db import models
from pygments.lexers import get_lexer_by_name, get_all_lexers
from pygments.formatters.html import HtmlFormatter
from pygments import highlight
from pygments.styles import get_all_styles
import uuid


LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


# Create your models here.
def get_identifier():
    return str(uuid.uuid4())[:8]


class Person(models.Model):
    class Meta:
        verbose_name = "person"
        verbose_name_plural = "persons"
        ordering = ('name',)

    name = models.CharField(
        verbose_name='Name',
        max_length=120,
        blank=False,
        null=False
    )

    identifier = models.CharField(
        verbose_name='Identifier',
        default=get_identifier(),
        max_length=8
    )

    def __str__(self):
        return self.name


class Snippet(models.Model):
    class Meta:
        verbose_name = 'snippet'
        verbose_name_plural = 'snippets'
        ordering = ('created',)

    created = models.DateTimeField(
        auto_now_add=True
    )
    title = models.CharField(
        max_length=100,
        blank=True,
        default=''
    )
    code = models.TextField()
    linenos = models.BooleanField(
        default=False
    )
    language = models.CharField(
        choices=LANGUAGE_CHOICES,
        default='python',
        max_length=100
    )
    style = models.CharField(
        choices=STYLE_CHOICES,
        default='friendly',
        max_length=100
    )
    owner = models.ForeignKey(
        'auth.User',
        related_name='snippets'
    )
    highlighted = models.TextField()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):

        lexer = get_lexer_by_name(self.language)
        linenos = self.linenos and 'table' or False
        options = self.title and {'title': self.title} or {}
        formatter = HtmlFormatter(style=self.style, linenos=linenos,
                                  full=True, **dict(options))
        self.highlighted = highlight(self.code, lexer, formatter)
        super(Snippet, self).save(*args, **kwargs)
