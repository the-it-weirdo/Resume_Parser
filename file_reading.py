import os
import PyPDF2

def get_files(dir_name:str, format:str):
    # create a list of file and sub directories 
    # names in the given directory 
    dir_list = os.listdir(dir_name)
    all_files = list()
    
    # Iterate over all the entries
    for entry in dir_list:
        # Create full path
        full_path = os.path.join(dir_name, entry)
        
        # If entry is a directory then get the list of files in this directory 
        if os.path.isdir(full_path):
            all_files = all_files + get_files(full_path, format)
        else:
            if format in entry:
                all_files.append(full_path)
                
    return all_files

def load_files(files_list:list):
    file_datas = []
    # iterate over all file in list
    for sfile in files_list:
        # if file is in pdf format, read pdf
        if sfile[-4:] == '.pdf':
            file_datas.append(__read_pdf__(sfile))
    return file_datas
    

def __read_pdf__(file_path):
    pdf_data = []
    # open file
    with open(file_path, 'rb') as open_file:
        # create pdf reader object
        pdf_reader = PyPDF2.PdfFileReader(open_file)
        # iterate over all pages in the file
        for i in range(pdf_reader.numPages):
            # add page text to list
            pdf_data += [pdf_reader.getPage(i).extractText()]
    return pdf_data