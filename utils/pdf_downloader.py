import os
import urllib.request


def save_pdf(pdf_url : str , paper_id : str , folder="data/papers"):
    os.makedirs(folder , exist_ok=True)             # --- Creeate folder if missing ---
    filename = f"{paper_id}.pdf"                    # --- filename ---
    
    filepath = os.path.join(folder , filename)

    urllib.request.urlretrieve(pdf_url , filepath)

    return filepath