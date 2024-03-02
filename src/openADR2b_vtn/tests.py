import uuid
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class MyModelTests(APITestCase):
    def setUp(self):
        # self.headers = {"Content-Type": "application/xml"}
        oadrVenName = "testVen"
        self.request_id = str(uuid.uuid4())
        self.correct_ven_registration_request = f"""<?xml version="1.0" encoding="utf-8"?>
        <oadr:oadrPayload xmlns:oadr="http://openadr.org/oadr-2.0b/2012/07">
            <oadr:oadrSignedObject xmlns:oadr="http://openadr.org/oadr-2.0b/2012/07" oadr:Id="oadrSignedObject">
                <oadr:oadrCreatePartyRegistration ei:schemaVersion="2.0b" xmlns:ei="http://docs.oasis-open.org/ns/energyinterop/201110">
                    <requestID xmlns="http://docs.oasis-open.org/ns/energyinterop/201110/payloads">{self.request_id}</requestID>
                    <oadr:oadrProfileName>2.0b</oadr:oadrProfileName>
                    <oadr:oadrTransportName>simpleHttp</oadr:oadrTransportName>
                    <oadr:oadrTransportAddress>None</oadr:oadrTransportAddress>
                    <oadr:oadrReportOnly>false</oadr:oadrReportOnly>
                    <oadr:oadrXmlSignature>false</oadr:oadrXmlSignature>
                    <oadr:oadrVenName>{oadrVenName}</oadr:oadrVenName>
                    <oadr:oadrHttpPullModel>true</oadr:oadrHttpPullModel>
                </oadr:oadrCreatePartyRegistration>
            </oadr:oadrSignedObject>
        </oadr:oadrPayload>
        """

    def test_party_registration(self):
        url = reverse("EiRegisterParty_url_path")

        response = self.client.post(
            url,
            data=self.correct_ven_registration_request,
            content_type="application/xml",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        assert "reg_id_002" in response.content.decode()
        assert "test_vtn" in response.content.decode()
        assert self.request_id in response.content.decode()
