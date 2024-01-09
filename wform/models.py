from django.db import models

from wagtailmetadata.models import MetadataPageMixin
from wagtail.fields import RichTextField
from modelcluster.fields import ParentalKey
from wagtail.models import Page, Orderable
from wagtail.admin.panels import (
    FieldPanel, FieldRowPanel,
    InlinePanel, MultiFieldPanel
)
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField

from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from wagtailcaptcha.models import WagtailCaptchaEmailForm
from wagtail.fields import StreamField, RichTextField
from django.utils.functional import cached_property
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel, FieldRowPanel
from django.contrib import messages
from django.shortcuts import redirect
from django.http import HttpResponseRedirect



class FormField(AbstractFormField):
    page = ParentalKey('FormPage', on_delete=models.CASCADE, related_name='form_fields')


class FormPage(WagtailCaptchaEmailForm):
    thank_you_text = models.TextField("Gracias por tu mensaje", blank=True)

    content_panels = AbstractEmailForm.content_panels + [
        InlinePanel("form_fields", label="Form fields"),
        FieldPanel("thank_you_text", classname="full"),
        MultiFieldPanel(
            [
                FieldRowPanel(
                    [
                        FieldPanel("from_address", classname="col6"),
                        FieldPanel("to_address", classname="col6"),
                    ]
                ),
                FieldPanel("subject"),
            ],
            "Email Notification Config",
        ),
    ]


    def get_context(self, request, *args, **kwargs):
        context = super(FormPage, self).get_context(request, *args, **kwargs)
        # context["blog_page"] = self.blog_page
        return context
    
    def serve(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = self.get_form(request.POST, page=self, user=request.user)

            if form.is_valid():
                self.process_form_submission(form)

                thank_you_message = self.thank_you_text
                if thank_you_message:
                    messages.success(request, thank_you_message)

                home_page = Page.objects.filter(depth=2).first()
                if home_page:
                    return HttpResponseRedirect(home_page.url)

        return super().serve(request, *args, **kwargs)