# File: main.py
import argparse
from converter import clean_doi, get_metadata_from_doi # <-- Mengimpor dari "kamar mesin"

def process_dois_from_file(input_path, output_path, format_type):
    """Fungsi utama untuk memproses DOI dari file."""
    print(f"Membaca DOI dari: {input_path}")
    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            raw_dois = f.readlines()
    except FileNotFoundError:
        print(f"Error: File tidak ditemukan di '{input_path}'")
        return

    cleaned_dois = sorted(list(set([clean_doi(d) for d in raw_dois if clean_doi(d)])))
    
    if not cleaned_dois:
        print("Tidak ada DOI valid yang ditemukan dalam file.")
        return

    print(f"Ditemukan {len(cleaned_dois)} DOI unik untuk diproses.")
    print("-" * 40)

    successful_entries = []
    failed_dois = []

    for doi in cleaned_dois:
        metadata = get_metadata_from_doi(doi, format_type)
        if metadata:
            successful_entries.append(metadata)
        else:
            failed_dois.append(doi)
        print("-" * 40)

    # Menyimpan hasil
    if successful_entries:
        with open(output_path, "w", encoding="utf-8") as f:
            f.write("\n\n".join(successful_entries))
        print(f"🎉 Berhasil! {len(successful_entries)} referensi disimpan di: {output_path}")

    if failed_dois:
        fail_path = "failed_dois.txt"
        with open(fail_path, "w", encoding="utf-8") as f:
            f.write("\n".join(failed_dois))
        print(f"🟡 {len(failed_dois)} DOI gagal diproses. Lihat daftarnya di: {fail_path}")

if __name__ == "__main__":
    # Bagian ini mengatur agar skrip bisa menerima perintah dari terminal
    parser = argparse.ArgumentParser(description="Konverter DOI ke format referensi (RIS/BibTeX).")
    parser.add_argument("--input", required=True, help="Path ke file .txt yang berisi daftar DOI.")
    parser.add_argument("--output", required=True, help="Path untuk menyimpan file hasil.")
    parser.add_argument("--format", choices=['RIS', 'BibTeX'], default='RIS', help="Format output (RIS atau BibTeX).")
    
    args = parser.parse_args()
    
    process_dois_from_file(args.input, args.output, args.format)
