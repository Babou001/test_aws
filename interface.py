from flask import Flask, render_template, request, redirect, url_for
import os
import model

app = Flask(__name__)

# Définir un dossier pour stocker les fichiers téléversés
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Créer le dossier de téléversement s'il n'existe pas
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/compare', methods=['POST'])
def compare():
    if 'image1' not in request.files or 'image2' not in request.files:
        return redirect(url_for('index'))

    file1 = request.files['image1']
    file2 = request.files['image2']

    if file1.filename == '' or file2.filename == '':
        return redirect(url_for('index'))

    # Sauvegarder les fichiers dans le dossier de téléversement
    file1_path = os.path.join(app.config['UPLOAD_FOLDER'], 'temp_image1.jpg')
    file2_path = os.path.join(app.config['UPLOAD_FOLDER'], 'temp_image2.jpg')
    file1.save(file1_path)
    file2.save(file2_path)

    # Comparer les visages
    result = model.compare_faces(file1_path, file2_path)
    
    message = "Les visages correspondent !" if result else "Les visages ne correspondent pas."
    return render_template('result.html', message=message, image1='uploads/temp_image1.jpg', image2='uploads/temp_image2.jpg')

if __name__ == '__main__':
    app.run(debug=True, port=8081)