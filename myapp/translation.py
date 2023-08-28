from modeltranslation.translator import register, TranslationOptions
from .models import AppBar, Portell, Landing, Body, Contact, Message

@register(AppBar)
class AppBarTranslationOptions(TranslationOptions):
    fields = ('home', 'about', 'wines', 'contact')

@register(Portell)
class PortellTranslationOptions(TranslationOptions):
    fields = ('name', 'type', 'alcohol', 'variety', 'description')

@register(Landing)
class LandingTranslationOptions(TranslationOptions):
    fields = ('text', 'description', 'caption', 'button')

@register(Body)
class BodyTranslationOptions(TranslationOptions):
    fields = ('text', 'title', 'description')

@register(Contact)
class ContactTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

@register(Message)
class MessageTranslationOptions(TranslationOptions):
    fields = ('first', 'second', 'third', 'fourth')


