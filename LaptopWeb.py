import streamlit as st
import pickle
import numpy as np
import math
#loading the data and model
pipe=pickle.load(open('pipe.pkl','rb'))
df=pickle.load(open('data_lap.pkl','rb'))

st.title("LAPTOP PRICE PREDICTOR")
st.image('lap.jpg')

#####
col1,col2=st.columns(2)
col3,col4=st.columns(2)
col5,col6=st.columns(2)
col7,col8=st.columns(2)
col9,col10=st.columns(2)
col11,col12=st.columns(2)


#####

#brand
with col1:
    company = st.selectbox('Brand', df['Company'].unique())

#Typename
with col2:
    type = st.selectbox('TypeName', df['TypeName'].unique())

#RAM
with col3:
    ram = st.selectbox('RAM (in GB)', [2, 4, 6, 8, 12, 16, 24, 32, 64])

#weight
with col4:
    weight = st.number_input('Weight of LAP')

#Touchscreen
with col5:
    touch = st.selectbox('TouchScreen', ['No', 'Yes'])

#IPS
with col6:
    ips = st.selectbox('IPS', ['No', 'Yes'])

#screen size
with col7:
    screen = st.number_input('ScreenSize')

#resolution
with col8:
    resolution = st.selectbox('Resolution',
                              ['1920x1080', '1366x768', '1600x900', '3840x2160', '3200x1800', '2880x1800', '2560x1600',
                               '2560x1440', '2304x1440'])

#cpu
with col9:
    cpu = st.selectbox('CPU Brand', df['Cpu_brand'].unique())

#hdd
with col10:
    hdd = st.selectbox('HDD (in GB)', [0, 128, 256, 512, 1024, 2048])

#ssd
with col11:
    ssd = st.selectbox('SSD (in GB)', [0, 128, 256, 512, 1024])

#gpu brand
with col12:
    gpu = st.selectbox('GPU Brand', df['Gpu Brand'].unique())


#os
os = st.selectbox('OS', df['os'].unique())

if st.button("Price"):
    #conversion
    ppi=None
    if touch=='Yes':
        touch=1
    else:
        touch=0
    if ips=='Yes':
        ips=1
    else:
        ips=0
    #PPI calculation
    x_res=int(resolution.split('x')[0])
    y_res=int(resolution.split('x')[1])
    ppi=(((x_res**2)+(y_res**2))**0.5)/screen


    query=np.array([company, type, ram, weight, touch,ips,ppi,
       cpu, hdd, ssd, gpu, os])
    query=query.reshape((1,12))
    #the price is log transformed during training so we have to take exp
    st.title("The Predicted price of "+company+" for this Configuration RS."+str(int(np.exp(pipe.predict(query)[0]))))