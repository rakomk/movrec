import pandas as pd
import streamlit as st
import numpy as np
import os
import shutil
import glob
from bing_image_downloader import downloader



st.header('This is a header')

movie_df = pd.read_csv('recomandesmovie.csv')
movie_df['title']=movie_df.title.str.replace(':',' ')
movie_df['title']=movie_df.title.str.replace(';',' ')


fevmovi= pd.read_csv('fevmovi.csv')
fevmovi['title']=fevmovi.title.str.replace(':',' ')
fevmovi['title']=fevmovi.title.str.replace(';',' ')

age = st.slider('How old are you?', 1, 499,25)


how = st.slider('How many are you?', 4, 12,4)
def load_images():
    image_files = glob.glob("new/DATASET/*/*.jpg")
    manuscripts = []
    for image_file in image_files:
        image_file = image_file.replace("\\", "/")
        parts = image_file.split("/")
        if parts[1] not in manuscripts:
            manuscripts.append(parts[1])
    manuscripts.sort()
    return image_files, manuscripts

def load_imagesold():
    image_files = glob.glob("new/DATASETtwo/*/*.jpg")
    manuscripts = []
    for image_file in image_files:
        image_file = image_file.replace("\\", "/")
        parts = image_file.split("/")
        if parts[1] not in manuscripts:
            manuscripts.append(parts[1])
    manuscripts.sort()
    return image_files, manuscripts
if st.button('predict'):
  bb=os.listdir('new/DATASETtwo')  
  cc=os.listdir('new/DATASET')
  if len(cc) or len(bb)!=0:
    for i in bb:
        directory = i
        parent = "new/DATASETtwo/"
        path = os.path.join(parent, directory)
        shutil.rmtree(path)	
    for j in cc:    
        directory = j
        parent = "new/DATASET/"
        path = os.path.join(parent, directory)
        shutil.rmtree(path) 
  if how==12:
   new=how*age
   nor=4*age
   old=age-1
   new_a=old*how
   st.write(how)
   #st.dataframe(movie_df[new_a:new])
   #st.dataframe(fevmovi[nor-4:nor])

   st.write('FAVRITE MOVIES')



   for i in fevmovi[nor-4:nor].title.values:
    downloader.download("{0} movie poster".format(i), limit=1,  output_dir='new/DATASETtwo', adult_filter_off=True, force_replace=False, timeout=60)
   image_files, manuscripts = load_imagesold()
   view_manuscripts = os.listdir('new/DATASETtwo')
   n = 4
   view_images = []
   for image_file in image_files:
    if any(manuscript in image_file for manuscript in view_manuscripts):
        view_images.append(image_file)
   groups = []
   for i in range(0, len(view_images), n):
    groups.append(view_images[i:i+n])

   for group in groups:
    cols = st.columns(n)
    for i, image_file in enumerate(group):
        cols[i].image(image_file)
   
   
   st.write('RECOMANDED MOVIES')


   for i in movie_df[new_a:new].title.values:
    downloader.download("{0} movie poster".format(i), limit=1,  output_dir='new/DATASET', adult_filter_off=True, force_replace=False, timeout=60)
   image_files, manuscripts = load_images()
   view_manuscripts = os.listdir('new/DATASET')
   n = 4
   view_images = []
   for image_file in image_files:
    if any(manuscript in image_file for manuscript in view_manuscripts):
        view_images.append(image_file)
   groups = []
   for i in range(0, len(view_images), n):
    groups.append(view_images[i:i+n])

   for group in groups:
    cols = st.columns(n)
    for i, image_file in enumerate(group):
        cols[i].image(image_file)








  elif how==4:
   new=12*age
   nor=4*age
   old=age-1
   new_a=old*12
   m=(movie_df[new_a:new])
   mp=(fevmovi[nor-4:nor]) 
   #st.dataframe(m[:4])
   #st.dataframe(mp) 

   st.write('FAVRITE MOVIES')


   for i in mp.title.values:
    downloader.download("{0} movie poster".format(i), limit=1,  output_dir='new/DATASETtwo', adult_filter_off=True, force_replace=False, timeout=60)
   image_files, manuscripts = load_imagesold()
   view_manuscripts = os.listdir('new/DATASETtwo')
   n = 4
   view_images = []
   for image_file in image_files:
    if any(manuscript in image_file for manuscript in view_manuscripts):
        view_images.append(image_file)
   groups = []
   for i in range(0, len(view_images), n):
    groups.append(view_images[i:i+n])

   for group in groups:
    cols = st.columns(n)
    for i, image_file in enumerate(group):
        cols[i].image(image_file)

   st.write('RECOMANDED MOVIES')

   for i in m[:4].title.values:
    downloader.download("{0} movie poster".format(i), limit=1,  output_dir='new/DATASET', adult_filter_off=True, force_replace=False, timeout=60) 
   image_files, manuscripts = load_images()
   view_manuscripts = os.listdir('new/DATASET')
   n = 4
   view_images = []
   for image_file in image_files:
    if any(manuscript in image_file for manuscript in view_manuscripts):
        view_images.append(image_file)
   groups = []
   for i in range(0, len(view_images), n):
    groups.append(view_images[i:i+n])

   for group in groups:
    cols = st.columns(n)
    for i, image_file in enumerate(group):
        cols[i].image(image_file)







  elif how==8:
   new=12*age
   nor=4*age
   old=age-1
   new_a=old*12
   m=(movie_df[new_a:new])
   mp=(fevmovi[nor-4:nor]) 
   #st.dataframe(m[:8])
   #st.dataframe(mp)  

   st.write('FAVRITE MOVIES')

   for i in mp.title.values:
    downloader.download("{0} movie poster".format(i), limit=1,  output_dir='new/DATASETtwo', adult_filter_off=True, force_replace=False, timeout=60)
   image_files, manuscripts = load_imagesold()
   view_manuscripts = os.listdir('new/DATASETtwo')
   n = 4
   view_images = []
   for image_file in image_files:
    if any(manuscript in image_file for manuscript in view_manuscripts):
        view_images.append(image_file)
   groups = []
   for i in range(0, len(view_images), n):
    groups.append(view_images[i:i+n])

   for group in groups:
    cols = st.columns(n)
    for i, image_file in enumerate(group):
        cols[i].image(image_file)


   st.write('RECOMANDED MOVIES')


   for i in m[:8].title.values:
    downloader.download("{0} movie poster".format(i), limit=1,  output_dir='new/DATASET', adult_filter_off=True, force_replace=False, timeout=60)
   image_files, manuscripts = load_images()
   view_manuscripts = os.listdir('new/DATASET')
   n = 4
   view_images = []
   for image_file in image_files:
    if any(manuscript in image_file for manuscript in view_manuscripts):
        view_images.append(image_file)
   groups = []
   for i in range(0, len(view_images), n):
    groups.append(view_images[i:i+n])

   for group in groups:
    cols = st.columns(n)
    for i, image_file in enumerate(group):
        cols[i].image(image_file)










