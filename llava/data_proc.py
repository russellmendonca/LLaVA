from tqdm import tqdm
import requests
import json

def download_file_with_progress(url, file_path):
    """
    Function to download a file from a given URL with a progress bar and save it to the specified file path.
    :param url: str. The URL from where to download the file.
    :param file_path: str. The file path where to save the downloaded file.
    """
    # Send a GET request to the URL
    response = requests.get(url, stream=True)
    # Get the total file size from headers
    total_size = int(response.headers.get('content-length', 0))
    
    # Open the file path for writing in binary mode
    with open(file_path, 'wb') as file, tqdm(
        desc=file_path,
        total=total_size,
        unit='iB',
        unit_scale=True,
        unit_divisor=1024,
    ) as bar:
        for data in response.iter_content(chunk_size=1024):
            size = file.write(data)
            bar.update(size)

def download_url_data():
    # Replace this list with tuples of actual URLs and file paths
    urls_to_download = [
        # ('http://example.com/train2017.zip', 'train2017.zip'),
        # ('http://example.com/other_dataset.zip', 'other_dataset.zip'),
        # Add more tuples (url, file_path) as needed
        ('http://images.cocodataset.org/zips/train2017.zip', 'coco_train2017.zip')
        # ('http://images.cocodataset.org/zips/val2014.zip', 'coco_val2014.zip')

    ]

    for url, file_path in urls_to_download:
        download_file_with_progress(url, file_path)

def filter_json_data(image_key, inp_path, out_path):
    """
    Load data from a JSON file, filter it to keep only entries where 'image' attribute contains 'coco/train2017/',
    and save the filtered data to a new JSON file.
    :param file_path: str. The path to the input JSON file.
    """
    # Load the JSON data from the file
    with open(inp_path, 'r') as file:
        data = json.load(file)

    # Filter out entries where 'image' attribute does not contain 'coco/train2017/'
    filtered_data = []
    for entry in data:
        if 'image' in entry and image_key in entry['image']:
            filtered_data.append(entry)
    
    # Save the filtered data to a new JSON file
    with open(out_path, 'w') as f:
        json.dump(filtered_data, f, indent=2)
        

if __name__ == '__main__':
    pass
    #filter_json_data('coco/train2017', '../playground/data/llava_v1_5_mix665k.json', '../playground/data/llava_v1_5_coco_train2017.json')