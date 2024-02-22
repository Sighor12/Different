import streamlit as st
import os
import time
import glob
import os
from gtts import gTTS
from PIL import Image

st.title("pagina web de sonido")
image = Image.open('calavera con color.png')

st.image(image,width=200)

try:
  os.mkdir("temp")
except:
  pass

st.subheader("Texto a audio")
st.write('las interfaces de texto a audio son muy necesarias para las interfaces multimodales ya que permiten '
         'una comunicación más accesible y natural, facilitando la inclusión de personas con discapacidades '
         'visuales y permitiendo la interacción en situaciones donde no es posible leer texto. estas interfaces '
         'también impulsan tecnologías emergentes como los asistentes de voz inteligentes, haciendo que la tecnología '
         'sea más accesible e intuitiva para todos los usuarios')

