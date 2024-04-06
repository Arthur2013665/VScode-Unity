import requests
import os
import sys

def download_file(url, output_path):
    try:
        # Make a GET request to the URL
        response = requests.get(url)
        if response.status_code == 200:
            # Write the content to the output file
            with open(output_path, 'wb') as f:
                f.write(response.content)
            print(f"File downloaded successfully to: {output_path}")
        else:
            print(f"Failed to download file: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    if len(sys.argv) != 3:
        print("Usage: python downloader.py <URL> <output_path>")
        sys.exit(1)

    url = sys.argv[1]
    output_path = sys.argv[2]

    download_file(url, output_path)

if __name__ == "__main__":
    main()
