import os
import aspose.words as aw

def convert_docx_to_html_file(file_path, output_file):
    doc = aw.Document(file_path)
    doc.save(output_file)
