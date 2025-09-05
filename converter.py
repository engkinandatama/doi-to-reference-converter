# File: converter.py
import requests
import re
import time
from urllib.parse import quote

def clean_doi(raw_doi):
    """Membersihkan string input untuk mendapatkan DOI yang valid."""
    if not raw_doi: return None
    cleaned = re.sub(r'https?://(dx\. )?doi\.org/', '', raw_doi.strip())
    cleaned = re.sub(r'^(doi:)\s*', '', cleaned, flags=re.IGNORECASE)
    match = re.search(r'(10\..+)', cleaned)
    if match:
        return match.group(1).strip().rstrip('.')
    return None

def get_metadata_from_doi(doi, output_format='RIS'):
    """Mencoba mengambil metadata dari berbagai sumber."""
    format_map = {
        'RIS': 'application/x-research-info-systems',
        'BibTeX': 'application/x-bibtex'
    }
    content_type = format_map.get(output_format, 'application/x-research-info-systems')

    # 1. Coba Crossref
    try:
        print(f"➡️ Mencoba Crossref untuk: {doi}")
        headers = {'Accept': content_type}
        url = f"https://api.crossref.org/works/{doi}/transform"
        params = {'mailto': 'library.script@example.com'} # 'Polite pool'
        response = requests.get(url, headers=headers, params=params, timeout=15 )
        if response.status_code == 200 and response.text.strip():
            print(f"✅ Berhasil ditemukan di Crossref.")
            return response.text
        print(f"🟡 Tidak ditemukan di Crossref (Status: {response.status_code}).")
    except requests.exceptions.RequestException as e:
        print(f"⚠️ Gagal menghubungi server Crossref: {e}")

    # 2. Coba DataCite
    try:
        print(f"➡️ Mencoba DataCite...")
        headers = {'Accept': content_type}
        url = f"https://api.datacite.org/dois/{doi}"
        response = requests.get(url, headers=headers, timeout=15 )
        if response.status_code == 200 and response.text.strip():
            print(f"✅ Berhasil ditemukan di DataCite.")
            return response.text
        print(f"🟡 Tidak ditemukan di DataCite.")
    except requests.exceptions.RequestException as e:
        print(f"⚠️ Gagal menghubungi server DataCite: {e}")

    print(f"❌ Gagal total untuk DOI: {doi}.")
    return None
