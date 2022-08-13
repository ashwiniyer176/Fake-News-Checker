import imp
import pdfkit
from flask import make_response

def createPdf(webData):
    pdf = pdfkit.from_string(webData)
    response = make_response(pdf)
    response.headers["Content-Type"] = "application/pdf"
    response.headers["Content-Disposition"] = "inline; filename=Report.pdf"
    return response
