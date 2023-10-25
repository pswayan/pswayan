from flask import Flask, request, jsonify, send_from_directory
import os


app = Flask(__name__)

# Set the upload folder
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

DOWNLOAD_FOLDER = 'downloads'
app.config['DOWNLOAD_FOLDER'] = DOWNLOAD_FOLDER

# Create the upload folder if it doesn't exist
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

if not os.path.exists(DOWNLOAD_FOLDER):
    os.makedirs(DOWNLOAD_FOLDER)
    

# Define the route for uploading files
@app.route('/upload', methods=['POST'])
def upload_file():
    # Get the uploaded file
    file = request.files['file']

    # Save the file to the upload folder
    file.save(os.path.join(UPLOAD_FOLDER, file.filename))

    # Return a success response
    return jsonify({'message': 'File uploaded successfully'})

# Define the route for downloading files
@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    print("Requested filename:", filename)
    print("Path to file:", os.path.join(UPLOAD_FOLDER, filename))
    if not os.path.exists(os.path.join(UPLOAD_FOLDER, filename)):
        return jsonify({'message': 'File not found'}), 404
      
    return send_from_directory(UPLOAD_FOLDER, filename, as_attachment=True)   


if __name__ == '__main__':
    app.run(debug=True)
