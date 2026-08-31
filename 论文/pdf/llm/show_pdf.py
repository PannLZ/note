from pypdf import PdfReader
import sys

pdf_path = "CAMEF.pdf"
reader = PdfReader(pdf_path)
print(f"Total pages: {len(reader.pages)}")

for i, page in enumerate(reader.pages):
    text = page.extract_text()
    if text:
        print(f"\n{'='*60}")
        print(f"PAGE {i+1}")
        print(f"{'='*60}")
        print(text[:3000])  # Print first 3000 chars per page
        if len(text) > 3000:
            print("... [truncated]")
