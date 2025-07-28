import fitz  # PyMuPDF

def extrair_texto_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    texto_total = ""

    for i, page in enumerate(doc):
        texto = page.get_text()
        texto_total += f"\n--- Página {i+1} ---\n{texto}"

    return texto_total

if __name__ == "__main__":
    texto = extrair_texto_pdf("Relatorio Serasa Talmany Dantas.pdf")
    print(texto)
