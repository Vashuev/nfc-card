from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ContactForm
from .serializers import ContactFormSerializer
from django.core.mail import send_mail
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

def new_contact_form_submitted_mail(obj):
    try:
        subject = "Contact Form | New Entry"
        message = (
            f"Name: {obj.name}\n"
            f"Contact Number: {obj.phone_number}\n"
            f"Email: {obj.email}\n"
            f"Comment: {obj.comment}\n"
        )
        recipient_email = obj.email  # Email to send the confirmation
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [recipient_email], fail_silently=False)
        logger.info("Sent Contact Form email successfully!")
    except Exception as e:
        logger.error(f"Error while sending email: {e}")

class ContactFormAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ContactFormSerializer(data=request.data)
        if serializer.is_valid():
            contact_form = serializer.save()  # Save the data to the database
            new_contact_form_submitted_mail(contact_form)  # Send email
            return Response({"message": "Contact form submitted successfully."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        return Response({"error": "GET method is not allowed on this endpoint."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
