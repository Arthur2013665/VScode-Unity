from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    # Extract data from the form
    url = request.form['url']
    output_path = request.form['output_path']
    
    try:
        # Make a GET request to the specified URL
        response = requests.get(url)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Write the content to the output file
            with open(output_path, 'wb') as f:
                f.write(response.content)
            
            # Return success message
            return jsonify({'success': True, 'message': 'File downloaded successfully'})
        else:
            # Return error message if download fails
            return jsonify({'success': False, 'message': 'Failed to download file'})
    except Exception as e:
        # Return error message if an exception occurs
        return jsonify({'success': False, 'message': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
