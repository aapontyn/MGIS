#Assn 4
#Name: Alina Luce
#Date: 04/25/2018

# Write Python script to export selected map pages of your map to a PDF file and
# create a new PDF that includes the Title, Overview, and your exported pages.

# import arcpy and set up your workspace and environments
import arcpy
import os
arcpy.env.workspace = r"C:\EsriPress\Python\Data\Assignment4_Starter\Data"

# create an arcpy.mapping.MapDocument using your mxd
mxd = "C:/EsriPress/Python/Data/Assignment4_Starter/Assignment4_MapBook.mxd"
mapdoc = arcpy.mapping.MapDocument(mxd)

# Export your Data Driven Pages to a PDF file
# provide the path and file name of the PDF so that all pages will be exported

# create a fresh pdf document that will hold all of your pages
# use PDFDocumentCreate(pdf_path) function

pdfPath = r"C:\EsriPress\Python\Data\Assignment4_Starter\Final_Assn4.pdf"
if os.path.exists(pdfPath):
    os.remove(pdfPath)

pdfDoc = arcpy.mapping.PDFDocumentCreate(pdfPath)
pdfDoc.appendPages(r"C:\EsriPress\Python\Data\Assignment4_Starter\PDFs Assn4.pdf")
pdfDoc.appendPages(r"C:\EsriPress\Python\Data\Assignment4_Starter\Assignment4_MapBook.pdf")

# append the title page, the index pages, and the map pages to the PDF map book in that order
## My title and index pages are saved together in one PDF file

#use PDFDocumentCreate function's updateDocProperties method to update the mapbook title and authorship
pdfDoc.updateDocProperties(pdf_title = "NST MapBook", pdf_author = "Alina Pontynen Luce")

#save and close the mapbook
#this is IMPORTANT - the changes made to the mapbook won't be saved if the script
#is closed before executing saveAndClose()

pdfDoc.saveAndClose()

#delete reference to mapBookPDF
del pdfDoc

print "All done!"