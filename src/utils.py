
import os

def upload_to_uc_volume(catalog: str, schema: str, volume: str, local_file_path: str) -> str:
    
    """
    Uploads a local file to a Unity Catalog Volume so remote Spark can read it.
    
    Args:
        catalog: Target Unity Catalog name (e.g., "main").
        schema: Target schema name (e.g., "default").
        volume: Staging volume name (e.g., "raw").
        local_file_path: Relative path to the local file.
        
    Returns:
        str: The remote volume path (e.g., /Volumes/main/default/raw/file.csv).
    """

    if not os.path.exists(local_file_path):
        raise FileNotFoundError(f"Missing file: {local_file_path}")

    from databricks.sdk import WorkspaceClient
    w = WorkspaceClient()

    # 1. Ensure infrastructure exists
    w.statement_execution.execute_statement(statement=f"CREATE SCHEMA IF NOT EXISTS {catalog}.{schema}")
    w.statement_execution.execute_statement(statement=f"CREATE VOLUME IF NOT EXISTS {catalog}.{schema}.{volume}")

    # 2. Upload file
    file_name = os.path.basename(local_file_path)
    dest_path = f"/Volumes/{catalog}/{schema}/{volume}/{file_name}"
    
    print(f"Uploading {file_name} to {dest_path}...")
    with open(local_file_path, "rb") as f:
        w.files.upload(dest_path, f, overwrite=True)
        
    return dest_path