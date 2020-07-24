import pandas as pd
import os
folder = r'D:\Files\excel' #папка с файлами
files = [os.path.join(folder,f) for f in folder] #формируем список путей к файлам
all_file_frames = [] #сюда будем добавлять прочитанную таблицу 
for f in files:
    print('Reading %s'%f)
    tab = pd.read_excel(f)
    all_file_frames.append(tab)
all_frame = pd.concat(all_file_frames,axis=0) #  axis=0 если нужно добавить таблицу снизу и axis=1 если нужно слева
all_frame.to_excel('final_file.xlsx') #получим файл final_file.xlsx в os.getcwd()