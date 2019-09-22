import os

directory = 'Fotos_sin_match_guionbajo'
for filename in os.listdir(directory):
    archivo = filename[0:len(filename)-4]
    dir = f"{directory}/{archivo}"
    os.makedirs(dir)
    os.rename(f"{directory}/{filename}", f"{dir}/{filename}")
