import PyPDF2


def extract_pages_from_pdf(file_name, pages_to_extract):
    # Open the PDF file
    pdf_reader = PyPDF2.PdfReader(file_name)

    # Create a PDF writer object
    pdf_writer = PyPDF2.PdfWriter()

    # Loop through the list of pages to extract
    for page_num in pages_to_extract:
        # Get a single page object
        page = pdf_reader.pages[page_num - 1]  # Note: PyPDF2 uses 0-based page numbering

        # Add the page to the PDF writer object
        pdf_writer.add_page(page)

    # Create a new PDF file to save the extracted pages
    output_file_name = "extracted_pages.pdf"
    with open(output_file_name, "wb") as output_pdf:
        pdf_writer.write(output_pdf)

    print(f"Extracted pages {pages_to_extract} from {file_name} and saved it as {output_file_name}")


if __name__ == "__main__":
    # The name of the PDF file to extract from
    file_name = "example.pdf"

    # List of pages to extract (1-based numbering)
    pages_to_extract = [1, 3, 5]

    extract_pages_from_pdf(file_name, pages_to_extract)
