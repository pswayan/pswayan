from flask import Flask, request, jsonify, send_from_directory
import os


app = Flask(__name__)

# Set the upload folder
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Create the upload folder if it doesn't exist
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
    

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
@app.route('/download/<filename>')
def download_file(filename):
    # Check if the file exists
    if not os.path.exists(os.path.join(UPLOAD_FOLDER, filename)):
        return jsonify({'message': 'File not found'}), 404

    # Send the file to the user
    return send_from_directory(UPLOAD_FOLDER, filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
