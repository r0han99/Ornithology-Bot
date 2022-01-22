import streamlit as st 
import hydralit_components as hc
import os 
from itertools import cycle
from pathlib import Path
import base64


# fonts

font_url0 = '''<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Lora:wght@700&display=swap" rel="stylesheet">'''
fontname0 = "Lora"

font_url1 = '''<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Lora:wght@700&family=Zilla+Slab:ital,wght@0,700;1,600&display=swap" rel="stylesheet">'''
fontname1 = "Zilla Slab"


def sup_titles(name):
    
    
    html_string = f"<p style='text-align:center; font-weight:bold; font-size:40px; font-family:{fontname1};'>{name}</p>"
    return html_string


def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded


def cs_gallery(gallery_path):


    st.markdown(sup_titles("Gallery"),unsafe_allow_html=True)

    exp = st.expander('Beta Notice')
    exp.warning('*** The current Gallery just displays all the Images in the Repository, the future versions of this application will include Multiple levels of Categorization such as Habitat, Regions, Apperances and So on. ***')


    bird_names = os.listdir(gallery_path)
    bird_names.remove('.DS_Store')
    
    

    cols = st.columns(3)
    image_indexes = cycle([0,1,2])
    

    for i in range(315): 
        bird = ' '.join(list(map(str.capitalize, bird_names[i].split('-'))))
        image = os.path.join(gallery_path,bird_names[i],'1.jpg')
        cols[next(image_indexes)].image(image,use_column_width=True,caption=bird)
        
    
def cs_identify():

    st.markdown(sup_titles("Identification"),unsafe_allow_html=True)


    # model instantiation 
    model_path = '/Users/Shared/Relocated/Others/Code/Data Science/Bird-Encyclopedia/EfficientNetB3-birds-98.92.h5'
    model_name = 'EfficientNetB3-bird'
    acc = 98.92


    # Image Augmentation 


    # Model Prediction 


    # Parse the Information to Info-Collection Pipeline 


    # call Information Rendering Pipeline

    pass


def cs_encylopedia():

    st.markdown(sup_titles("Bird Encyclopedia"),unsafe_allow_html=True)




if __name__ == '__main__':

    # Galleria Path 
    gallery_path = './data/gallery-files'

    

    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.set_page_config(page_title="Ornithologia",layout="wide",initial_sidebar_state="collapsed", page_icon='./assets/origami.png')

    st.markdown(font_url0,unsafe_allow_html=True)
    st.markdown(font_url1,unsafe_allow_html=True)
    

    menu_data = [

    {'icon': "fa fa-book", 'label':"Encylopedia", "ttip":"Ton of Visualisations"},
    {'icon': "fa fa-cogs", 'label':"Identification", "ttip":"Here lies the power of Machine Learning"},
    {'icon': "fa fa-camera-retro", 'label':"Gallery",'ttip':"Great Pictures"}, 
    # {'icon': "far fa-copy", 'label':"Right End"},
    ]

    # we can override any part of the primary colors of the menu
    #over_theme = {'txc_inactive': '#FFFFFF','menu_background':'red','txc_active':'yellow','option_active':'blue'}
    over_theme = {'txc_inactive': 'black','menu_background':'#f7f7f7','txc_active':'#4478FB'}
    menu_id = hc.nav_bar(menu_definition=menu_data,home_name='About',override_theme=over_theme,sticky_nav=True,sticky_mode='jumpy',hide_streamlit_markers=False,)


    # st.markdown("<center><span style='font-family:georgia;font-size:55px; font-weight:bold;'> <i>Ornithologia</i>🦉 — Bot</span></center>",unsafe_allow_html=True)
    st.markdown(f"<h1 style='font-family:georgia; font-size:59px; font; text-align:center;  '><i>Ornithologia  </i><img src='data:image/png;base64,{img_to_bytes('./assets/origami.png')}' class='img-fluid' width=62 height=62> — Bot</h1>",unsafe_allow_html=True)
    st.markdown('***')




    if menu_id == 'Gallery':
        
        cs_gallery(gallery_path)

    elif menu_id == 'Identification':

        cs_identify()

    elif menu_id == 'Encylopedia':

        cs_encylopedia()



