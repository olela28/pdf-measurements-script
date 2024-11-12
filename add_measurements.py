import os
import fitz  # PyMuPDF

def add_measurements_to_pdf(input_pdf, output_pdf, measurements):
    pdf_document = fitz.open(input_pdf)
    page = pdf_document[0]

    # Get all text blocks on the page
    text_blocks = page.get_text("blocks")

    # Initialize the reference block for "Declaration" as None
    declaration_block = None

    # Find the "Declaration" block by checking the text content in each block
    for block in text_blocks:
        if "Declaration" in block[4]:  # Block text is in the 5th element of the block tuple
            declaration_block = block
            break

    # If the "Declaration" block was found, position "Size" directly below it
    if declaration_block:
        # Position below the "Declaration" block
        y = declaration_block[3] + 15  # Start below the Declaration text
        x_key = declaration_block[0]   # Align "Size" with "Declaration" key's x position

        # Offset for the value to align it with other values
        x_value = declaration_block[2] + 10  # Fine-tune as needed

        font_size = 10

        # Insert "Size" in bold at the calculated x_key position
        size_text = "Size"
        page.insert_text((x_key, y), size_text, fontsize=font_size, color=(0, 0, 0))

        # Insert the measurement value at the calculated x_value position
        remaining_text = measurements.split("Size")[1].strip()
        page.insert_text((x_value, y), remaining_text, fontsize=font_size, color=(0, 0, 0))

    # Save the updated PDF
    pdf_document.save(output_pdf)
    pdf_document.close()

def process_pdfs(input_directory, output_directory): 
    # Create the output directory if it doesn't exist
    os.makedirs(output_directory, exist_ok=True)

    for filename in os.listdir(input_directory):
        input_path = os.path.join(input_directory, filename)

        # Check the product name to decide which measurements to add
        if "TEASTAR" in filename.upper() or "BAG@100" in filename.upper():
            measurements = "Size                                                            1 BAG@100 GR"
        elif "CADDY" in filename:
            measurements = "Size                                                            5x20 BAGS"
        elif "LEAFCUP" in filename:
            measurements = "Size                                                            1 TEABAG, CASE = 90 BAGS"
        elif "BAG@250" in filename:
            measurements = "Size                                                            1 BAG@250 GR"
        else:
            continue  # Skip files that don't match

        # Define output path in the specified output directory
        output_path = os.path.join(output_directory, f"updated_{filename}")

        # Add measurements to the PDF
        add_measurements_to_pdf(input_path, output_path, measurements)

# Specify the input and output directories
input_pdf_directory = "C:/Users/lao/Desktop/automation/pdf_files"  # Location of input PDFs
output_pdf_directory = "C:/Users/lao/Desktop/automation/updated_files"  # Location for updated PDFs
process_pdfs(input_pdf_directory, output_pdf_directory)
