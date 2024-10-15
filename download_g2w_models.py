import os
import requests
import zipfile
import tqdm
# current_dir = os.path.dirname(os.path.abspath(__file__))
# model_dir = os.path.join(current_dir, 'G2PWModel')
# print("g2pw model_dir: ", model_dir)
def download_and_decompress(model_dir: str='/opt/program/GPT_SoVITS/text/'):
    parent_directory = os.path.dirname(model_dir)
    print("g2pw model_dir: ", parent_directory)
    # zip_dir = os.path.join(parent_directory,"G2PWModel_1.1.zip")
    extract_dir = os.path.join(parent_directory,"G2PWModel_1.1")
    extract_dir_new = os.path.join(parent_directory,"G2PWModel")
    print("Downloading g2pw model...")
    modelscope_url = "https://paddlespeech.bj.bcebos.com/Parakeet/released_models/g2p/G2PWModel_1.1.zip"
    with requests.get(modelscope_url, stream=True) as r:
        r.raise_for_status()
        with open("G2PWModel_1.1.zip", 'wb') as f:
            for chunk in tqdm.tqdm(r.iter_content(chunk_size=8192)):
                if chunk:
                    f.write(chunk)

    print("Extracting g2pw model...")
    with zipfile.ZipFile("./G2PWModel_1.1.zip", "r") as zip_ref:
        zip_ref.extractall(parent_directory)

    os.rename(extract_dir, extract_dir_new)

    return model_dir

if __name__ == "__main__":
    download_and_decompress()