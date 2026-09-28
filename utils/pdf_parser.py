import pymupdf
import re

def extract_text(pdf_path: str) -> str:

    doc = pymupdf.open(pdf_path)
    text = ""

    for page in doc:
        # sort=True keeps reading order
        text += page.get_text("text", sort=True) + "\n"

    doc.close()

    # Remove noisy tokens from figures/examples
    text = re.sub(r"<pad>|<EOS>", "", text)
    text = re.sub(r"\n{2,}", "\n\n", text)

    return text.strip()