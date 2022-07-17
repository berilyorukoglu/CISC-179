FileList = ["file1.pdf", "file2.docx", "file3.xlsx", "file4.pdf", "file5.doc", "file6.xls", "file7.pdf"]

for item in FileList:
    if item.endswith("pdf"):
        print(item)