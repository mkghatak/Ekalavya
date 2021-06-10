#!/usr/bin/env python
# coding: utf-8

# In[9]:


pip install PyPDF2


# In[27]:


import requests, PyPDF2

url = 'https://www.tataconsumer.com/docs/default-source/default-document-library/tcpl---integrated-annual-report-2020-21.pdf?sfvrsn=0'
response = requests.get(url)
my_raw_data = response.content

with open("my_pdf.pdf", 'wb') as my_data:
    my_data.write(my_raw_data)


open_pdf_file = open("my_pdf.pdf", 'rb')
read_pdf = PyPDF2.PdfFileReader(open_pdf_file)
num_pages = read_pdf.getNumPages()

ann_text = []
for page_num in range(num_pages):
    if read_pdf.isEncrypted:
        read_pdf.decrypt("")
        #print(read_pdf.getPage(page_num).extractText())
        read_pdf.getPage(page_num).extractText()
        page_text = read_pdf.getPage(page_num).extractText().split()
        ann_text.append(page_text)

    else:
        #print(read_pdf.getPage(page_num).extractText())
        read_pdf.getPage(page_num).extractText()

        
#print(ann_text)

wordlist = ann_text
wordfreq = []
for w in wordlist:
    wordfreq.append(wordlist.count(w))
    
print("List\n" + str(wordlist) + "\n")
print("Frequencies\n" + str(wordfreq) + "\n")
print("Pairs\n" + str(list(zip(wordlist, wordfreq))))


# In[ ]:




