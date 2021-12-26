import streamlit as st 
import hydralit_components as hc
import os 
from itertools import cycle








def cs_gallery():

    bird_names = os.listdir('./data/galleria')
    bird_names.remove('.DS_Store')
    
    orgcol = st.columns([5,1])
    orgcol[0].markdown('***Gallery***')
    rndbtn = orgcol[1].empty()
    

    multiples = []
    pairs = []
    for i in range(1,36):
        multiples.append(9*i)
    multiples.append(0)
    

    for _ in range(18):
        temp = []
        for i in range(2):
            temp.append(multiples.pop(0))
        print(temp)
        pairs.append(temp)

    pairs.insert(0,[0,9])
    pairs[-1::] = [315]


    


 
    cols = st.columns(3)
    image_indexes = cycle([0,1,2])

    pairs = cycle(pairs)

    if rndbtn.button('Generate'):
        
        try:
            for i in range(*next(pairs)): 
                bird = ' '.join(list(map(str.capitalize, bird_names[i].split('-'))))
                image = os.path.join('./data/galleria',bird_names[i],'0.jpg')
                cols[next(image_indexes)].image(image,use_column_width=True,caption=bird)
        except:
            for i in range(next(pairs)): 
                bird = ' '.join(list(map(str.capitalize, bird_names[i].split('-'))))
                image = os.path.join('./data/galleria',bird_names[i],'0.jpg')
                cols[next(image_indexes)].image(image,use_column_width=True,caption=bird)
                
        
        
    













if __name__ == '__main__':

    # Galleria Path 
    # gallery_path = './data/galleria'

    

    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.set_page_config(page_title="Ornithologia",layout="wide",initial_sidebar_state="collapsed", page_icon='🕊️')

    

    menu_data = [

    {'icon': "fa fa-book", 'label':"Bird Encylopedia", "ttip":"Ton of Visualisations"},
    {'icon': "fa fa-cogs", 'label':"Identification", "ttip":"Here lies the power of Machine Learning"},
    {'icon': "fa fa-camera-retro", 'label':"Gallery",'ttip':"Great Pictures"}, 
    # {'icon': "far fa-copy", 'label':"Right End"},
    ]

    # we can override any part of the primary colors of the menu
    #over_theme = {'txc_inactive': '#FFFFFF','menu_background':'red','txc_active':'yellow','option_active':'blue'}
    over_theme = {'txc_inactive': 'black','menu_background':'#F5F5F5','txc_active':'#058DFC'}
    menu_id = hc.nav_bar(menu_definition=menu_data,home_name='About',override_theme=over_theme,sticky_nav=True,hide_streamlit_markers=False,)


    st.markdown("<center><span style='font-family:georgia;font-size:55px; font-weight:bold;'> <i>Ornithologia</i>🦉 — Bot</span></center>",unsafe_allow_html=True)
    st.markdown('***')



    if menu_id == 'Gallery':

        cs_gallery()




