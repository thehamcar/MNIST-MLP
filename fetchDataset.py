import kagglehub
import os
import shutil

data_dir = os.path.join(os.path.dirname(__file__), "data")
os.makedirs(data_dir, exist_ok=True)

cache_path = kagglehub.dataset_download("hojjatk/mnist-dataset")

print("Cache path:", cache_path)

for file in os.listdir(cache_path):
    src_file = os.path.join(cache_path, file)
    dst_file = os.path.join(data_dir, file)
    
    if os.path.isfile(src_file):
        shutil.copy2(src_file, dst_file)
        print(f"Copied {file} to {data_dir}")

print(f"All dataset files copied to {data_dir}")