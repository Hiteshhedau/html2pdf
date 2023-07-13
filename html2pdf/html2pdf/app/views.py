from django.shortcuts import render
from django.http import HttpResponse


def html_to_pdf(request):
    html_file='app/resume.html'
    with open(html_file, 'r') as file:
        html_content = file.read()
    
    import os
    os.add_dll_directory(r"C:\msys64\usr\bin")
    from weasyprint import HTML

    # Convert HTML to PDF using WeasyPrint
    pdf_bytes = HTML(string=html_content).write_pdf()

    # Create a Django HTTP response with PDF content
    response = HttpResponse(pdf_bytes, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="resume.pdf"'

    return response
 
    


