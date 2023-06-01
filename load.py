import os
import aspose.words as aw

def convert_docx_to_html_file(file_path, output_file):
    doc = aw.Document(file_path)
    doc.save(output_file)

docx_file = "E:\dowload\Test_Docx.docx"
output_file = 'output.html'
current_directory = os.getcwd()
output_path = os.path.join(current_directory, output_file)
convert_docx_to_html_file(docx_file, output_path)