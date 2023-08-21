import s3fs
import zarr
import dotenv
import os

dotenv.load_dotenv()




def get_store(repo_name, branch_name, zarr_store_path):
    access_key_id = os.getenv("LAKEFS_ACCESS_KEY_ID")
    secret_access_key = os.getenv("LAKEFS_SECRET_ACCESS_KEY")
    endpoint_url  = os.getenv("LAKEFS_ENDPOINT_URL")
    url = f"s3://{repo_name}/{branch_name}/{zarr_store_path}"
    fs = s3fs.S3FileSystem(key=access_key_id, secret=secret_access_key, client_kwargs={'endpoint_url':endpoint_url})
    return zarr.open(s3fs.S3Map(url, s3=fs))


if __name__=="__main__":
    repo_name = "try-zarr"
    zarr_store_path = "example.zarr"
    
    store_main = get_store(repo_name=repo_name, branch_name="main", zarr_store_path=zarr_store_path)
    print(f"In main branch store_main[2][2] = {store_main[2][2]}")

    store_dev = get_store(repo_name=repo_name, branch_name="dev", zarr_store_path=zarr_store_path)
    print(f"In dev branch store_dev[2][2] = {store_dev[2][2]}")