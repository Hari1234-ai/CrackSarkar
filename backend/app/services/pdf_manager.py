import os
import fitz # PyMuPDF
from typing import Dict, List, Optional, Tuple

class PDFManager:
    """Manages PDF analysis, text extraction, and billingual support."""
    
    def __init__(self, pdf_dir: str = "sources/pdfs/"):
        # Auto-detect path (if run from root or from backend folder)
        if not os.path.exists(pdf_dir) and os.path.exists(os.path.join("backend", pdf_dir)):
            self.pdf_dir = os.path.join("backend", pdf_dir)
        else:
            self.pdf_dir = pdf_dir
            
    def list_books(self) -> List[str]:
        """Lists all PDFs available in the source directory."""
        if not os.path.exists(self.pdf_dir):
            print(f"[DEBUG] PDF Directory not found: {os.path.abspath(self.pdf_dir)}")
            return []
        return [f for f in os.listdir(self.pdf_dir) if f.lower().endswith(".pdf")]
    
    def analyze_pdf(self, filename: str) -> Dict:
        """Analyzes a PDF to check for text vs images and likely language."""
        path = os.path.join(self.pdf_dir, filename)
        try:
            doc = fitz.open(path)
            num_pages = len(doc)
            
            # Check first few pages for selectable text
            has_text = False
            total_chars = 0
            for i in range(min(5, num_pages)):
                text = doc[i].get_text().strip()
                if text:
                    has_text = True
                    total_chars += len(text)
            
            # Simple heuristic for language detection
            # (Checking for Telugu unicode ranges)
            is_telugu = False
            if has_text:
                first_page_text = doc[0].get_text()
                # Telugu Unicode range: 0C00–0C7F
                telugu_chars = [c for c in first_page_text if '\u0c00' <= c <= '\u0c7f']
                if len(telugu_chars) > (total_chars * 0.1): # If > 10% are Telugu chars
                    is_telugu = True
                    
            status = "Searchable" if has_text else "Scanned (Image-based)"
            lang = "Telugu" if is_telugu else "English/Other"
            
            return {
                "filename": filename,
                "status": status,
                "language": lang,
                "pages": num_pages,
                "is_searchable": has_text
            }
        except Exception as e:
            return {"error": str(e)}

    def extract_text(self, filename: str, start_page: int = 0, end_page: int = -1) -> str:
        """Extracts raw text from a searchable PDF with robust error handling."""
        if not filename.lower().endswith(".pdf"):
            return ""
            
        path = os.path.join(self.pdf_dir, filename)
        if not os.path.exists(path):
            return ""
            
        try:
            # We open with a check to prevent MuPDF syntax errors from crashing/logging excessively
            doc = fitz.open(path)
            if doc.is_closed or doc.is_encrypted:
                return ""
                
            if end_page == -1:
                end_page = len(doc)
            
            content = ""
            for i in range(start_page, min(end_page, len(doc))):
                content += doc[i].get_text() + "\n\n"
            doc.close()
            return content
        except Exception:
            # Silently fail for extraction so the next book can be tried
            return ""
