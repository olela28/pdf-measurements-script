import os
import fitz
def add_measurements_to_pdf(input_pdf, output_pdf, measurements):
    pdf_document = fitz.open(input_pdf)
    page = pdf_document[0]

    x, y = 50, 50
    font_size = 12

    page.insert_text((x,y), measurements, fontsize=font_size, color=(0, 0, 0))

    pdf_document.save(output_pdf)
    pdf_document.close()

def process_pdfs(directory):
    for filename in os.listdir(directory):
        input_path = os.path.join(directory, filename)

        if "Teastar" in filename:
            measurements = "1 BAG@100 GR"
        elif "Tea-Caddy" in filename:
            measurements = "5x20 BAGS"
        elif "LeafCup" in filename:
            measurements = "EA = 1 TEABAG, CASE = 90 BAGS"

            output_path = os.path.join(directory, f"updated_{filename}")

            add_measurements_to_pdf(input_path, output_path, measurements)

    pdf_directory = "C:/Users/lao/Desktop/PDF File_Automation"
    process_pdfs(pdf_directory)