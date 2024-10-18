# Pdf-measurements-script
This script automates the process of adding specific product measurements to PDF files based on the product name found in the filenames.
This is particularly useful for businesses that need to update files in bulk.

# Features
- Automatically scans a directory of PDF files.
- Adds measurements to the first page of PDFs based on product names.
- Supports condition-based logic for different product categories.
- Easy to customize and extend for other products or measurements.

# Prerequisites
- Python 3.x
- PyMuPDF
You can install the required library using:<br>
``pip install pymupdf``

# Usage
1. Clone the Repository:<br>


   ``git clone https://github.com/your-username/pdf-measurement-updater.git``<br>
   ``cd pdf-measurement-updater``
2. Adjust the conditions in the script if you want to change the measurement values or product identifiers.
3. Run the script:

To add measurements to all PDFs in a specific directory, run: <br>


``python add_measurements.py`` <br>

Make sure to specify the correct directory path iniside the script. <br>

4. Example File Names:
   - TEASTAR.pdf -> The script will add the measurement 1 BAG@100 GR.
   - LEAFCUP.pdf -> The script will add the measurement 1 TEABAG, CASE 90 BAGS.
   - CADDY.pdf -> The script will add the measurement 5x20 BAGS.
  
# Code Explanation
The script scans a directory for PDF files and applies measurement test based on conditions. <br>
It uses the "fitz" module from PyMuPDF to open, modify, and save PDFs:

``import os`` <br>
``import fitz`` <br>
``def add_measurements_to_pdf(input_pdf, output_pdf, measurements):`` <br>

See add_measurements.py file for the rest of the code.


# Example Output
The script will create new PDF files with the prefix "updated_" , like:
- updated_TEASTAR.pdf
- updated_LEAFCUP.pdf

# Troubleshooting
- No text added: Check that the filenames match the conditions you've set in the script.
- Permission errors: Ensure the script has write permissions in the directory.

# License
The project is licensed under the MIT License - see the LICENSE file for details.

# Contributing 
Feel free to submit issues or pull requests if you have any improvements or suggestions.
Contributions are welcome!


