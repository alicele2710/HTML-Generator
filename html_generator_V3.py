#!/usr/bin/env python
# coding: utf-8

# In[3]:


get_ipython().run_line_magic('cd', '"C:/Users/alicele/Desktop/Springboard/project1"')
import pandas as pd
import csv
from collections import defaultdict


df = pd.read_csv('IDQ_V1.csv') 
#define functions to convert each data cell to html
col1 = lambda x: "<td><span style=\"color: rgb(255,0,0)\">Yes</span></td>" if int(x) == 1 else "<td> <span style=\"color: rgb(42, 170, 82)\">No</span></td>"
col4to6 = lambda x: "<td><span style=\"color: rgb(255,0,0)\">&#x2716;</span></td>" if int(x) == 0 else "<td> <span style=\"color: rgb(42, 170, 82)\">&#10004;</span></td>"
def col2to3(x):
    if int(x) < 3:
        return "<td><span style=\"color: rgb(255,0,0)\">"+str(x)+"</span></td>"
    elif int(x) < 4:
        return "<td><span style=\"color: rgb(189,183,107)\">"+str(x)+"</span></td>"
    elif int(x) < 6:
        return "<td><span style=\"color: rgb(42,170,82)\">"+str(x)+"</span></td>"
    else:
        return "<td><span style=\"color: rgb(42,170,82)\">5+</span></td>"

#create dictionary with keys as contactids  
csvfile = open('IDQ_V1.csv', mode = 'r')
idq_by_contactid = defaultdict(list)
for row in csv.DictReader(csvfile):
    cid = row.pop('contactid')
    idq_by_contactid[cid].append(row)


df = []
#create html columns for 6 ASIN attributes 
for key, val in idq_by_contactid.items():
    upload = []
    for item in val:
        item['ASIN'] = "<td>" + item['asin'] + "</td>"
        item['search suppressed'] = col1(item['is_index_suppressed'])
        item['bullet points'] = col2to3(item['bullet_point_count'])
        item['product images'] = col2to3(item['qty_website_images'])
        item['product keywords'] = col4to6(item['has_keywords'])
        item['product description'] = col4to6(item['has_description'])
        item['leaf node'] = col4to6(item['has_leaf_node'])
        item['full_html'] = "<tr>"+item['ASIN']+item['search suppressed']+item['bullet points']+item['product images']+item['product keywords']+item['product description']+ item['leaf node']+"</tr>"
        upload.append(item['full_html'])
    df.append([key, ''.join(upload)])
final = pd.DataFrame(df, columns = ['contactid', 'upload'])
hd = '<html><head><style>table.pardot-table {font-family: calibri, sans-serif;  font-size: 10pt;  border-collapse: collapse;  width: 100%;}table.pardot-table td,table.pardot-table th {    border: 1px solid #212F3D;  text-align: left;  padding: 8px;}table.pardot-table th {background-color: #212F3D; color: #FF7733;}table.pardot-table tr:nth-child(even) {background-color: #fff;}table.pardot-table tr:nth-child(odd){background-color: #f4f5f5;}</style></head><body><table class=\"pardot-table\"><tr><th>ASIN</th><th>Search Suppressed</th><th>Bullet Points</th><th>Product Images</th><th>Product Keywords</th><th>Product Description</th><th>Leaf Node</th></tr>'

bt = '</table></body></html>'

final['upload'] = hd + final['upload']+bt

final.to_csv(r'C:/Users/alicele/Desktop/Springboard/project1/IDQ_upload_V4.csv',index = False)


# In[4]:


get_ipython().run_line_magic('pwd', '')


# In[ ]:




