# This is my first python code
print ('Sidhant')
print ('Hello! World')



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

if __name__ == '__main__':
    app.run(debug=True)
