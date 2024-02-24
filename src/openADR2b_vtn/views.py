import uuid
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views.generic import View
from django.shortcuts import render


@method_decorator(csrf_exempt, name="dispatch")
class EiRegisterPartyView(View):
    template_name = "EiRegisterParty.xml"

    def post(self, request):
        context = {
            "requestID":str(uuid.uuid4()),
            "registrationID": "reg_id_002",
            "venID": "ven_id_001",
            "vtnID": "test_vtn",
        }
        return render(
            request,
            self.template_name,
            context,
            content_type="application/xml; charset=utf-8",
        )
