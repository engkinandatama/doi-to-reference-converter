# DOI to Reference Converter

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg )](https://opensource.org/licenses/MIT )
[![Python Version](https://img.shields.io/badge/python-3.7%2B-blue.svg )](https://www.python.org/downloads/ )
[![made-with-colab](https://colab.research.google.com/assets/colab-badge.svg )]([https://colab.research.google.com/github/engkinandatama/doi-to-reference-converter/blob/main/DOI_Converter_Colab.ipynb](https://colab.research.google.com/drive/1N7qNXN9xmLRKzcV7IgvHPLrTNG2kwBrN?usp=sharing) )

A versatile Python tool to batch convert a list of DOIs (Digital Object Identifiers) into `.ris` or `.bib` reference files. Designed for researchers, students, and writers to streamline their reference management workflow.

This tool fetches metadata from multiple robust sources, including **Crossref**, **DataCite**, and **NCBI/PubMed**, ensuring a high success rate.

---

## ✨ Key Features

- **Batch Conversion**: Process hundreds of DOIs at once, instead of one by one.
- **Multiple Formats**: Export references in **RIS** (for Mendeley, Zotero, EndNote) or **BibTeX** (for LaTeX).
- **Flexible Input**: Accepts DOIs from a `.txt` file or direct copy-paste.
- **Dual Interface**:
  - 💻 **Web UI**: An easy-to-use graphical interface powered by Google Colab. No installation needed.
  - ⚙️ **CLI**: A powerful command-line interface for local use and automation.
- **Smart & Resilient**: Automatically falls back to other APIs if a source fails, and handles network errors gracefully.
- **Error Reporting**: Generates a `failed_dois.txt` file for any DOIs that could not be processed, so you never lose track.

---

## 🚀 Getting Started

You can use this tool in two ways: the simple Web UI on Google Colab or the more advanced Command-Line Interface (CLI) locally.

### Option 1: The Easy Way (Google Colab Web UI)

This is the recommended method for most users. It's quick, easy, and requires no local setup.

1.  **Open the Colab Notebook**:
    <a href="https://colab.research.google.com/github/engkinandatama/doi-to-reference-converter/blob/main/DOI_Converter_Colab.ipynb" target="_blank"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>
    *(Click the button above to open the tool directly in your browser )*

2.  **Run the Setup Cell**: Run the first code cell to prepare the environment.

3.  **Use the Interface**: An interactive UI will appear.
    - Upload your `.txt` file of DOIs or paste them into the text box.
    - Select your desired output format (`RIS` or `BibTeX`).
    - Click "Generate References".
    - Your files (`successful_references.ris` and `failed_dois.txt`) will be downloaded automatically.

### Option 2: The Power User Way (Command-Line Interface)

This method is for users who are comfortable with the terminal and want to run the tool locally.

#### 1. Prerequisites
- Python 3.7 or newer.
- Git.

#### 2. Installation
Clone the repository and install the required packages:
```bash
# Clone this repository
git clone https://github.com/engkinandatama/doi-to-reference-converter.git

# Navigate into the project directory
cd doi-to-reference-converter

# Install dependencies
pip install -r requirements.txt
```

#### 3. Usage
Run the script from your terminal. You must provide an input file and an output path.

**Basic Example:**
```bash
python main.py --input my_dois.txt --output my_references.ris --format RIS
```

**Arguments:**
- `--input`: (Required ) Path to the `.txt` file containing your list of DOIs (one per line).
- `--output`: (Required) Path where the output file will be saved.
- `--format`: (Optional) The desired output format. Choices are `RIS` or `BibTeX`. Defaults to `RIS`.

---

## 🏛️ Citation

This tool relies on several excellent public APIs for fetching metadata. If you use this tool in your research, please consider citing the primary data sources:

1.  **Crossref**:
    > Crossref. (2023). *The DOI® System for the Digital Age*. Crossref.org. Retrieved from [https://www.crossref.org](https://www.crossref.org )

2.  **DataCite**:
    > DataCite. (2023). *The Global Open Research Information Aggregator*. DataCite.org. Retrieved from [https://datacite.org](https://datacite.org )

3.  **NCBI/PubMed**:
    > National Center for Biotechnology Information. (2023). *PubMed*. National Library of Medicine. Retrieved from [https://pubmed.ncbi.nlm.nih.gov](https://pubmed.ncbi.nlm.nih.gov )

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
