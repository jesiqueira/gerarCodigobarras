import barcode
from barcode.writer import ImageWriter
import pandas as pd
import json
import os

bar_class = barcode.get_barcode_class('code128')
# barcode = 'BBM0000032502'

# writer=ImageWriter()
# code128 = bar_class(barcode, writer)
# code128.save('C:\Desenvolvimento\Gerar_cod_barras', {"module_width":.35, "module_height":10, "font_size": 9, "text_distance": 5, "quiet_zone": 3})

# code128.save('filename') # save the originally generated image

# to_be_resized = Image.open('filename.png') # open in a PIL Image object

# newSize = (500, 300) # new size will be 500 by 300 pixels, for example
# resized = to_be_resized.resize(newSize, resample=PIL.Image.NEAREST) # you can choose other :resample: values to get different quality/speed results

# resized.save('filename_resized.png') # save the resized image

# code128.save('filename1', {"module_width":.35, "module_height":10, "font_size": 12, "text_distance": 5, "quiet_zone": 3})

# -------------------Criar arquivo JSON-------------------------------------------
df = pd.read_excel("site.xlsx")
print(df.head())

df.to_json('arquivo.json')

# ---------------------------Carregar arquivo Json e Gerar etiquetas-----------------------
df = pd.read_json('arquivo.json')

# print(df['local'])
for d in df['local']:
  # bar_class = barcode.get_barcode_class('code128')
  barcode = d

  writer=ImageWriter()
  code128 = bar_class(barcode, writer)
  code128.save(d, {"module_width":.35, "module_height":10, "font_size": 9, "text_distance": 5, "quiet_zone": 3})


