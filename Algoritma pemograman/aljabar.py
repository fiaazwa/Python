# from docx import Document
# from similarity.ngram import NGram
 
# jum_huruf_min = 20 #kalimat terlalu pendek diabaikan
 
# #load file dan pindahkan ke memory
 
# def doc_to_text(nama_file):
#     doc = Document(nama_file)
#     fullText = []
#     for para in doc.paragraphs:
#         par = para.text.lower().strip()
#         if par != "" and len(par) > jum_huruf_min:
#             fullText.append(par)
 
#     #proses isi tabel
#     print("=======================")
#     tables = doc.tables
#     for table in tables:
#         for row in table.rows:
#             for cell in row.cells:
#                 for paragraph in cell.paragraphs:
#                     par = paragraph.text.lower().strip()
#                     if par != "" and len(par) > jum_huruf_min:
#                         fullText.append(par)
 
#     fullTextNoDup = list(set(fullText)) #buang duplikasi
#     fullTextNoDup.sort()  # sort supaya lebih mudah dicek
#     return fullTextNoDup 
 
# jum_gram = 4
# batas = 0.4 #threshold
# gram = NGram(jum_gram)
 
# dir = "C:\\yudiwbs\\dataset\\deteksi_plagiat\\"
# file1 = 'borang_nondik_standard_4.docx'
# file2 = 'borang_dik_standard_4.docx'
# file_out = "kesamaan_standard4.txt"
 
# list_par_doc1 = doc_to_text(dir+file1)
# list_par_doc2 = doc_to_text(dir+file2)
 
# file = open(dir+file_out, "w")
 
# for par1 in list_par_doc1:
#      for par2 in list_par_doc2:
#          jarak = gram.distance(par1, par2)
#          if ( jarak <=batas):
#              print(par1)
#              file.write(par1+"\n")
#              print(par2)
#              file.write(par2+"\n")
#              print(jarak)
#              file.write(str(jarak)+"\n")
#              print("--")
#              file.write("--\n")
#              file.flush()
 
# file.close()
# print("Selesai===") 
