from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from openADR2b_vtn.renderers import TemplateXMLRenderer
import xmltodict
import logging

logger = logging.getLogger(__name__)


def flatten_xml(message: str) -> str:
    lines = [line.strip() for line in message.split("\n")]
    return "".join(lines)


class EiRegisterPartyView(APIView):
    renderer_classes = [TemplateXMLRenderer]
    template_name = "EiRegisterParty.xml"

    def post(self, request):
        xml_data = request.body

        try:
            original_ven_message = xml_data.decode("utf-8")
            no_new_lines = flatten_xml(original_ven_message)
            message_dict = xmltodict.parse(no_new_lines, process_namespaces=False)
        except:
            logger.exception("Could not parse incoming message.")
            return Response(status=HTTP_400_BAD_REQUEST)

        try:
            ven_name = message_dict["oadr:oadrPayload"]["oadr:oadrSignedObject"][
                "oadr:oadrCreatePartyRegistration"
            ]["oadr:oadrVenName"]
            request_id = message_dict["oadr:oadrPayload"]["oadr:oadrSignedObject"][
                "oadr:oadrCreatePartyRegistration"
            ]["requestID"]
        except:
            logger.exception("Could not access required elements.")

        context = {
            "requestID": request_id,
            "registrationID": "reg_id_002",
            "venID": f"{ven_name}_001",
            "vtnID": "test_vtn",
        }
        return Response(context)
