from pathlib import Path
import sys

# Find PDF
pdf_path = Path("CAMEF.pdf")
if not pdf_path.exists():
    print("PDF not found")
    sys.exit(1)

try:
    from pypdf import PdfReader
    reader = PdfReader(str(pdf_path))
    print(f"Total pages: {len(reader.pages)}")
    
    # Extract text from all pages
    full_text = ""
    for i, page in enumerate(reader.pages):
        text = page.extract_text()
        if text:
            full_text += f"\n--- Page {i+1} ---\n"
            full_text += text
    
    # Save to file
    output_path = Path("CAMEF_extracted.txt")
    output_path.write_text(full_text, encoding="utf-8")
    print(f"Extracted text saved to {output_path}")
    print(f"Total characters: {len(full_text)}")
    
except Exception as e:
    print(f"Error: {e}")
    # Try alternative
    try:
        import PyPDF2
        reader = PyPDF2.PdfReader(str(pdf_path))
        print(f"Total pages (PyPDF2): {len(reader.pages)}")
        full_text = ""
        for i, page in enumerate(reader.pages):
            text = page.extract_text()
            if text:
                full_text += f"\n--- Page {i+1} ---\n"
                full_text += text
        output_path = Path("CAMEF_extracted.txt")
        output_path.write_text(full_text, encoding="utf-8")
        print(f"Extracted text saved to {output_path}")
    except Exception as e2:
        print(f"Alternative also failed: {e2}")
