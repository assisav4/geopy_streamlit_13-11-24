import kagglehub

# Download latest version
path = kagglehub.dataset_download("muhammadroshaanriaz/students-performance-dataset-cleaned")

print("Path to dataset files:", path)