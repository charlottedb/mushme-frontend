import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import io
import tensorflow as tf

species_list = ['Agaricus arvensis',
 'Agaricus augustus',
 'Agaricus bernardii',
 'Agaricus bisporus',
 'Agaricus bitorquis',
 'Agaricus bohusii',
 'Agaricus brunneolus',
 'Agaricus campestris',
 'Agaricus crocodilinus',
 'Agaricus cupreobrunneus',
 'Agaricus dulcidulus',
 'Agaricus impudicus',
 'Agaricus langei',
 'Agaricus lanipes',
 'Agaricus litoralis',
 'Agaricus moelleri',
 'Agaricus subfloccosus',
 'Agaricus subperonatus',
 'Agaricus sylvaticus',
 'Agaricus sylvicola',
 'Agaricus xanthodermus',
 'Amanita ceciliae',
 'Amanita citrina',
 'Amanita crocea',
 'Amanita excelsa',
 'Amanita franchetii',
 'Amanita fulva',
 'Amanita gemmata',
 'Amanita lividopallescens',
 'Amanita muscaria',
 'Amanita pantherina',
 'Amanita phalloides',
 'Amanita porphyria',
 'Amanita rubescens',
 'Amanita strobiliformis',
 'Amanita submembranacea',
 'Amanita vaginata',
 'Amanita virosa',
 'Boletus aereus',
 'Boletus edulis',
 'Boletus ferrugineus',
 'Boletus pinophilus',
 'Boletus reticulatus',
 'Boletus subtomentosus',
 'Clitocybe agrestis',
 'Clitocybe costata',
 'Clitocybe diatreta',
 'Clitocybe fragrans',
 'Clitocybe gibba',
 'Clitocybe metachroa',
 'Clitocybe nebularis',
 'Clitocybe odora',
 'Clitocybe phaeophthalma',
 'Clitocybe phyllophila',
 'Clitocybe rivulosa',
 'Clitocybe squamulosa',
 'Clitocybe vibecina',
 'Mycena abramsii',
 'Mycena acicula',
 'Mycena aetites',
 'Mycena amicta',
 'Mycena arcangeliana',
 'Mycena aurantiomarginata',
 'Mycena belliae',
 'Mycena capillaripes',
 'Mycena capillaris',
 'Mycena chlorantha',
 'Mycena cinerella',
 'Mycena citrinomarginata',
 'Mycena clavicularis',
 'Mycena clavularis',
 'Mycena crocata',
 'Mycena diosma',
 'Mycena epipterygia',
 'Mycena erubescens',
 'Mycena filopes',
 'Mycena flavescens',
 'Mycena galericulata',
 'Mycena galopus',
 'Mycena haematopus',
 'Mycena inclinata',
 'Mycena juniperina',
 'Mycena leptocephala',
 'Mycena luteovariegata',
 'Mycena megaspora',
 'Mycena meliigena',
 'Mycena metata',
 'Mycena olivaceomarginata',
 'Mycena pelianthina',
 'Mycena polygramma',
 'Mycena pseudocorticola',
 'Mycena pterigena',
 'Mycena pura',
 'Mycena purpureofusca',
 'Mycena renati',
 'Mycena rosea',
 'Mycena rosella',
 'Mycena rubromarginata',
 'Mycena sanguinolenta',
 'Mycena silvae-nigrae',
 'Mycena stipata',
 'Mycena stylobates',
 'Mycena tenerrima',
 'Mycena tintinnabulum',
 'Mycena vitilis',
 'Mycena vulgaris',
 'Russula acrifolia',
 'Russula adusta',
 'Russula aeruginea',
 'Russula amoenolens',
 'Russula atropurpurea',
 'Russula atrorubens',
 'Russula aurea',
 'Russula aurora',
 'Russula betularum',
 'Russula brunneoviolacea',
 'Russula caerulea',
 'Russula cessans',
 'Russula chloroides',
 'Russula claroflava',
 'Russula cuprea',
 'Russula curtipes',
 'Russula cyanoxantha',
 'Russula decolorans',
 'Russula delica',
 'Russula densifolia',
 'Russula depallens',
 'Russula emetica',
 'Russula faginea',
 'Russula farinipes',
 'Russula faustiana',
 'Russula fellea',
 'Russula foetens',
 'Russula fragilis',
 'Russula grata',
 'Russula graveolens',
 'Russula grisea',
 'Russula heterophylla',
 'Russula illota',
 'Russula insignis',
 'Russula integra',
 'Russula ionochlora',
 'Russula laccata',
 'Russula laeta',
 'Russula luteotacta',
 'Russula maculata',
 'Russula melliolens',
 'Russula nauseosa',
 'Russula nitida',
 'Russula nobilis',
 'Russula ochroleuca',
 'Russula odorata',
 'Russula olivacea',
 'Russula paludosa',
 'Russula parazurea',
 'Russula pelargonia',
 'Russula praetervisa',
 'Russula pseudointegra',
 'Russula puellaris',
 'Russula queletii',
 'Russula risigallina',
 'Russula romellii',
 'Russula rosea',
 'Russula roseoaurantia',
 'Russula sanguinea',
 'Russula sardonia',
 'Russula seperina',
 'Russula silvestris',
 'Russula solaris',
 'Russula sororia',
 'Russula subrubens',
 'Russula velenovskyi',
 'Russula versicolor',
 'Russula vesca',
 'Russula veternosa',
 'Russula violeipes',
 'Russula virescens',
 'Russula viscida',
 'Russula xerampelina']

def read_imagefile(file) -> Image.Image:
    image = Image.open(io.BytesIO(file))
    return image

def predict(image):
    #resize, predict and return prediction
    class_names = species_list
    img_array = np.asarray(image.resize((224, 224)))[..., :3]
    img_array = np.expand_dims(img_array, 0)
    
    predictions = model.predict(img_array)
    probabilities = tf.nn.softmax(predictions).numpy()[0]
    index_names = probabilities.argsort()[-5:][::-1]
    top_5_names = [class_names[i] for i in index_names if i < len(class_names)]
    top_5_probas =  [float(probabilities[i]) for i in index_names if i < len(class_names)]
    
    mushrooms = []
    
    for index, i in enumerate(top_5_names):
        mushroom = {}
        mushroom['Species'] = i
        mushroom['Probability'] = top_5_probas[index]
        mushrooms.append(mushroom)
    print(mushrooms)
    
    #for k,v in dict_mushrooms.items():
     #   proba_substrate = file.get_proba_species_criteria(name,'Substrate',user_input_substrate)
       # proba_month = file.get_proba_species_criteria(name,'Month',user_input_month)
      #  proba_habitat = file.get_proba_species_criteria(name,'Habitat',user_input_habitat)
        
        #Substrate.append(proba_substrate)
        #Habitat.append(proba_habitat)
        #Month.append(proba_month)
    
    return mushrooms




# loading model
model = tf.keras.models.load_model("./models_CNN_MobileNetV2.h5")

#SIDE BAR
logo = Image.open('new-logo.jpeg')
st.sidebar.image(logo, width=280, use_column_width=None)
st.sidebar.title('ABOUT')
st.sidebar.write("The aim of this project is to help fervent mushroom pickers to avoid intoxication. This model has been trained using the Danish Fungi Dataset.")
st.sidebar.write("This application was developped by four students in Data Science @LeWagon #batch619.")

st.sidebar.header('**DISCLAIMER**')
st.sidebar.write('_The results provided by this application are predictions and should be always be cross-validated by a mushroom expert before eating._')

#TITLE
st.title("MUSH ME")

#1st STEP
st.write('You went mushroom picking and you wonder if you can eat it? Verify it by yourself!')

st.header("DRAG & DROP YOUR PICTURE")         
uploaded_file = st.file_uploader("Choose a file", accept_multiple_files=True)

submit = st.button("Submit")
if submit:
    st.write("You succesfully uploaded your mushroom picture.")
    image_data = uploaded_file[0].read()
    img = Image.open(io.BytesIO(image_data))
    prediction = predict(img)
    st.write(prediction)
else :
    st.write("Sorry, something went wrong with your upload")   

#2ND STEP
st.header("LET THE MAGIC HAPPEN")

st.progress(2)


col1, col2 = st.beta_columns(2)
with col1:
    st.subheader('YOUR PICTURE')
    st.image(uploaded_file, width=None, use_column_width=None) 
with col2:
    st.subheader('OUR GUESS')
    st.image(uploaded_file, width=None, use_column_width=None)

#output display data

st.write('RESULTS')
st.write(pd.DataFrame({
'Mushroom Name': ['MODEL INPUT'],
'Probability': ['MODEL INPUT'],
'Edibility': ['MODEL INPUT'],
#'Comment': ['Careful, morel season is between september and october'],
}))


