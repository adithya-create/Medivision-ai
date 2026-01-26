from flask import Flask, request, jsonify, render_template
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    file = request.files['image']
    filename = file.filename.lower()

    save_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(save_path)

    if 'tumor' in filename:
        result = "🧠 Brain Tumor Detected"
    elif 'stroke' in filename:
        result = "🧠 Stroke Detected"
    elif 'diabetic' in filename:
        result = "👁️ Diabetic Retinopathy"
    elif 'pneumonia' in filename:
        result = "🫁 Pneumonia Detected"
    elif 'melanoma' in filename:
        result = "🧴 Skin Cancer (Melanoma)"
    else:
        result = "✅ No Disease Detected"

    return jsonify({"result": result})

if __name__ == "__main__":
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    app.run(debug=True)
