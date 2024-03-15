from django.contrib import admin
from app.models import Marker, QRCode, CrosswordQuestion
from django.http import HttpResponse
from PIL import Image
from io import BytesIO
import base64
import qrcode

# Register your models here.
admin.site.register(Marker)
admin.site.register(QRCode)
admin.site.register(CrosswordQuestion)

class QRCodeAdmin(admin.ModelAdmin):
    readonly_fields = ['qr_image_base64']
    change_form_template = 'admin/change_form_with_qr.html'

    def change_view(self, request, object_id, form_url='', extra_context=None):
        obj = self.get_object(request, object_id)
        if request.method == 'POST' and '_generate_qr_code' in request.POST:
            qr_image = qrcode.make(obj.link)
            qr_image_pil = qr_image.get_image()
            buffered = BytesIO()
            qr_image_pil.save(buffered, format="PNG")
            qr_image_base64 = base64.b64encode(buffered.getvalue()).decode('utf-8')
            obj.qr_image_base64 = qr_image_base64
            obj.save()
            extra_context = extra_context or {}
            extra_context['qr_image_base64'] = qr_image_base64
            extra_context['has_generated_qr'] = True
        return super().change_view(request, object_id, form_url=form_url, extra_context=extra_context)
