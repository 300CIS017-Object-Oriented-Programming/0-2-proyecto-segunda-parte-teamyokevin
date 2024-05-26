from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def generar_pdf(comprador):
    """
    Genera un archivo PDF con la información del comprador y recomendaciones para el evento.

    Parameters:
    comprador (Comprador): El objeto Comprador que contiene los datos del comprador.
    """
    # Crear un objeto canvas con tamaño de página carta
    c = canvas.Canvas("comprador.pdf", pagesize=letter)

    # Escribir los datos del comprador en el PDF
    c.drawString(100, 750, f"Nombre: {comprador.nombre}")
    c.drawString(100, 735, f"Apellido: {comprador.apellido}")
    c.drawString(100, 720, f"Edad: {comprador.edad}")
    c.drawString(100, 705, f"Correo: {comprador.correo}")
    c.drawString(100, 690, f"Teléfono: {comprador.telefono}")
    c.drawString(100, 675, f"Dirección: {comprador.direccion}")
    c.drawString(100, 660, f"Boletas: {comprador.boletas}")
    c.drawString(100, 645, f"Número de boletas compradas: {comprador.numero_boletas_compradas}")
    c.drawString(100, 630, f"Total de la compra: {comprador.total_compra}")

    # Escribir las recomendaciones para el evento en el PDF
    c.drawString(100, 600, "Recomendaciones para el evento:")
    c.drawString(100, 585, "1. Llega temprano para evitar filas.")
    c.drawString(100, 570, "2. No olvides tu boleta y tu identificación.")
    c.drawString(100, 555, "3. Sigue las indicaciones de seguridad del lugar.")
    c.drawString(100, 540, "4. Disfruta del evento!")

    # Guardar el archivo PDF
    c.save()

# Path: utils/pdf_generator.py