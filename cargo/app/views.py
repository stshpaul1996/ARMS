from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import HazardousMaterial, TransportRecord, Invoice
from .ocr_utils import extract_text_from_image
from .nlp_utils import extract_entities
from datetime import timezone

def upload_and_process_image(request):
    if request.method == 'POST' and request.FILES['document']:
        document = request.FILES['document']
        text = extract_text_from_image(document)
        entities = extract_entities(text)
        # Logic to handle entities and create transport records
        # Assuming entities contain relevant information
        return HttpResponse(f"Extracted Text: {text}<br>Entities: {entities}")
    return render(request, 'upload.html')

def display_placard(request, un_number):
    material = get_object_or_404(HazardousMaterial, un_number=un_number)
    return render(request, 'placard.html', {'material': material})

def generate_invoice(request, transport_record_id):
    transport_record = get_object_or_404(TransportRecord, id=transport_record_id)
    total_amount = calculate_total_amount(transport_record)
    invoice = Invoice.objects.create(
        transport_record=transport_record,
        # issued_at=timezone.utc(),
        total_amount=total_amount
    )
    return render(request, 'invoice.html', {'invoice': invoice})

def calculate_total_amount(transport_record):
    base_rate = 100.0
    return base_rate * transport_record.quantity
