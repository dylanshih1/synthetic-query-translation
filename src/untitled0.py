#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 22:51:53 2024

@author: dylanshih
"""

import fitz


class pdfParse:
    def __init__(self, file):
        self.file = file
        
    def parse(self):
        myList = []
        doc = fitz.open(self.file)
        number_of_pages = doc.page_count
        for i in range(0, number_of_pages):
            page = doc.load_page(i)
            text = page.get_text("json")
            myList.append(text)
            
        with open(self.file+".json", 'w', encoding="utf-8") as file:
            for i in myList:
                file.write(i)
            file.close()
        
if __name__=="__main__":
    pdf = pdfParse("synthetic-query-translation/data/0a65a2e79cf51e5370df4d4501658aa512e777bd.pdf")
    pdf.parse()