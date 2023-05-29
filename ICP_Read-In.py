import PyPDF2 as pdf

name_abbrev = "NL" # <<-- INPUT: Change according to your abbreviation for samples

with open("Data/ICP/Ergebnisse_Batch2.pdf", "rb") as f: # <<-- INPUT: Change name for input file - don't forget the file extension
    file_reader = pdf.PdfFileReader(f)
    pageObj = file_reader.getPage(0)
    content = pageObj.extractText()

header_start = content.find("Probenbez.")
header_end = content.find(name_abbrev, header_start)

header = content[header_start:header_end]
header = header.replace("Probenbez.", "").replace(",", ".")
header = header.split(" ")
best_header = []
best_header.append("Samples")
header = [item for item in header if item != '']
for i, element in enumerate(header):
    if i % 2 == 0:
        best_header.append(element +" " + header[i+1])

content = content[header_end:]
index = 0
lines = []
while index != -1:
    index = content.find(name_abbrev, 2)
    line = content[:index]
    lines.append(line)  
    content = content[index:]

lines[-1] = lines[-1].split("\n")[0]

with open("Data/ICP/Output.csv", "w") as f: # <<-- INPUT: Change name for output file - don't forget the file extension
    f.write(";".join(best_header) + "\n")
    for line in lines:
        line = line.replace(",", ".").replace(" ", ";")
        f.write(line + "\n")
    


