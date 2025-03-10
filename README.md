# Parcel Number Extractor

This project extracts parcel numbers from PDF documents containing tabular data and saves them into text files.

## Features
- Reads multiple PDF files from a specified input directory.
- Extracts tables containing parcel numbers using `pymupdf`.
- Cleans and processes extracted data using `pandas`.
- Saves parcel numbers to text files in a qgis query format.

## Installation
```sh
# Clone the repository
git clone https://github.com/yourusername/parcel-extractor.git
cd parcel-extractor

# Install dependencies
pip install pymupdf pandas
```

## Usage
```sh
# Place your PDF files in the `input_data` directory
# Run the script
python extract_parcels.py

# Extracted parcel numbers will be saved in the `output_data` directory as .txt files
```

## File Structure
```plaintext
parcel-extractor/
│── input_data/     # Directory for input PDFs
│── output_data/    # Directory for extracted parcel text files
│── extract_parcels.py  # Main script
│── README.md       # Project documentation
```

## License
This project is licensed under the MIT License.

