import os

# Imposta il link di base per le immagini su GitHub Pages
base_url = "https://tuo-username.github.io/gioco-volti/images/"  # Cambia con il tuo URL GitHub Pages

# Trova tutti i file nella cartella "images"
image_files = [f for f in os.listdir("images") if os.path.isfile(os.path.join("images", f))]

# Genera il codice JavaScript
js_code = "const images = [\n"
for image in image_files:
    name, ext = os.path.splitext(image)
    js_code += f'  {{ name: "{name}", src: "{base_url}{image}" }},\n'

js_code += "];"

# Salva il codice in un file JS
with open("images.js", "w") as f:
    f.write(js_code)

print("Codice JavaScript generato con successo!")
