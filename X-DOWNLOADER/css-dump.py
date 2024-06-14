import os
import requests

def download_css_files_from_list(file_path, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(file_path, 'r') as file:
        urls = file.read().splitlines()

        for url in urls:
            response = requests.get(url)

            if response.status_code == 200 and url.endswith('.css'):
                filename = os.path.join(output_dir, url.split('/')[-1])

                with open(filename, 'wb') as f:
                    f.write(response.content)

                print(f"Downloaded: {filename}")
            else:
                print(f"Failed to download CSS file from URL: {url}")

# Replace 'url-list.txt' with the actual file path containing the list of URLs
# Replace 'static/css' (output_dir) with the desired output directory
download_css_files_from_list('url-list.txt', 'static/css/')