import streamlit as st
import pandas as pd
from skimage.io import imread
import tensorflow as tf
from tensorflow.keras.applications.vgg19 import preprocess_input
from tensorflow.keras.models import Model
print(tf.__version__)

import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm

import glob
import ntpath
import cv2
import pathlib
from sklearn.metrics.pairwise import cosine_similarity
import scipy as sc
import elasticsearch
from elasticsearch import Elasticsearch

#########################################################
st.sidebar.subheader("SELECT SEARCH METHOD")
add_selectbox = st.sidebar.radio("  ",
    ("Image Similarilty", "Spotify annoy", "FAISS")
)

if add_selectbox == 'Image Similarilty' :
        st.title("Similarity Search")
        st.write("-------------------------------------------------------------------------------------------------")
        df=pd.read_csv('similarity_search.csv')
            
elif add_selectbox == 'Spotify annoy':
        st.title("Similar Products using Faiss - Facebook AI Similarity Search")
        st.write("-------------------------------------------------------------------------------------------------")
        
        
elif add_selectbox == 'FAISS':
    st.title("Similar Products using Faiss - Facebook AI Similarity Search")
    st.write("-------------------------------------------------------------------------------------------------")
    df=pd.read_csv('df.csv')

n=1
images = df['0'].unique()
temp= st.selectbox('Select', ['Select from dropdown','Upload a file'])
if temp== 'Select from dropdown':
    #images1 = df['second']
    st.subheader("Select a Product :")
    pic = st.selectbox('Choices:', images)
    st.write("**You selected:**")
    st.image(pic,width=None)
    t=[]
elif temp == 'Upload a file':
    try:
        pic=[]
        mfile= st.file_uploader("eadsx", accept_multiple_files=True)

        for file in mfile:
            p=file.name
            pic.append(p)
        for i in pic:
            st.image(i,width=None)
    except:
        st.write("errer")

count = 1
try:
    z = st.slider('Select Number of Similar Products:', 1, 9, 5)
    st.write("-------------------------------------------------------------------------------------------------")
    st.subheader("Output:")
    for index, row in df.iterrows():
        for i in pic:
            n=1
            if row['0']==i:
                st.write('**Similar Products for ** ', i)
                count=count+1
                while n < z+1:
                    st.image(row[n], use_column_width=None, caption=row[n])
                    n+=1
                st.write("-------------------------------------------------------------------------------------------------")
except:
    pass

