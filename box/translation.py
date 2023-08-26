from modeltranslation.translator import translator, TranslationOptions
from .models import OurModel


class OurmodelTrans(TranslationOptions):
    fields = ('name', 'fname', 'text')


# class ModelWithTranslator(OurModel):
#     fields = ('name', 'fname', 'text')


translator.register(OurModel, OurmodelTrans)

