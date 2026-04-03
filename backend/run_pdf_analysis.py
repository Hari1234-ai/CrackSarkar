import sys
import os

# Add the backend root to the Python path
backend_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(backend_dir)

from app.services.pdf_manager import PDFManager

def run_analysis():
    manager = PDFManager()
    books = manager.list_books()
    print(f"--- Analysis Report for {len(books)} Books ---")
    
    for book in books:
        result = manager.analyze_pdf(book)
        if "error" in result:
            print(f"[ERROR] {book}: {result['error']}")
        else:
            print(f"[{result['status']}] ({result['language']}) {book} - {result['pages']} pages")

if __name__ == "__main__":
    run_analysis()
