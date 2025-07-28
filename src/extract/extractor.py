import fitz  # PyMuPDF
from PIL import Image
import pytesseract
import os
import re

def extrair_texto_pdf(pdf_path: str) -> str:
    """
    Abre o PDF, converte cada página em imagem, aplica OCR e junta tudo em texto.
    """
    doc = fitz.open(pdf_path)
    texto_total = ""

    for i, page in enumerate(doc):
        pix = page.get_pixmap(dpi=300)
        img_path = f"pagina_{i}.png"
        pix.save(img_path)

        texto = pytesseract.image_to_string(Image.open(img_path), lang="por")
        texto_total += f"\n--- Página {i+1} ---\n{texto}"

        os.remove(img_path)

    return texto_total


def extrair_dados(texto: str) -> dict:
    """
    Procura no texto os campos importantes e tenta extrair seus valores.
    Usa regex e procura simples para extrair as informações.
    """

    def buscar_valor(campo, texto):
        # Tenta achar o campo e pegar o valor na mesma linha ou na próxima
        # Ajuste regex conforme padrão do seu PDF
        pattern = rf"{campo}[:\s]*([^\n\r]+)"
        match = re.search(pattern, texto, re.IGNORECASE)
        if match:
            return match.group(1).strip()
        return None

    campos = [
        "Serasa Score",
        "Anotações Negativas",
        "Anotacoes Negativas",
        "Renda Estimada",
        "Capacidade de pagamento",
        "Comprometimento de renda",
        "Histórico de Pagamento",
        "Historico de Pagamento",
        "Recomenda",
        "Limite mensal sugerido"
    ]

    dados = {}

    for campo in campos:
        valor = buscar_valor(campo, texto)
        # Corrige a chave para o padrão que você usa no prompt (remove acentos e minuscula)
        chave_normalizada = campo.lower().replace(" ", "_").replace("ç", "c").replace("ã", "a").replace("ó", "o").replace("ê", "e").replace("í", "i")
        dados[chave_normalizada] = valor

    return dados
