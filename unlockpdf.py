import pikepdf

def unlock_pdf(input_pdf, output_pdf, password=None):
    try:
        # Open the PDF with a password (if applicable)
        with pikepdf.open(input_pdf, password=password) as pdf:
            pdf.save(output_pdf)
        print(f"PDF unlocked successfully! Saved as {output_pdf}")
    except pikepdf.PasswordError:
        print("Failed to unlock PDF: invalid password or permissions.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage with password
input_pdf = "SB241014069.pdf"  # Replace with your PDF file
output_pdf = "unlocked.pdf"   # Replace with the desired output file name
password = "ESS21031995"  # Replace with the PDF password (if any)
unlock_pdf(input_pdf, output_pdf, password)
