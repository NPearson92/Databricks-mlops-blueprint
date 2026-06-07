
import os

def get_spark() -> "pyspark.sql.SparkSession":
    """
    Safely retrieves the Spark session while detecting the execution environment.
    Gracefully handles Databricks Workspaces, Databricks Connect, and local CI/CD pipelines.
    """
    # 1. Native Workspace / Jobs: Databricks Runtime is present in the environment
    if "DATABRICKS_RUNTIME_VERSION" in os.environ:
        print("[Env] Databricks Workspace or Job compute detected.")
        # In DBR, this safely returns the pre-configured global session
        from pyspark.sql import SparkSession
        return SparkSession.builder.getOrCreate()
    
    # 2. Local IDE: Try routing execution to the remote cluster via Databricks Connect
    try:
        from databricks.connect import DatabricksSession
        print("[Env] Local IDE detected. Routing via Databricks Connect.")
        return DatabricksSession.builder.getOrCreate()
        
    except ImportError:
        # 3. CI/CD or Offline: No Connect installed, spin up local PySpark for tests
        print("[Env] CI/CD or offline Python detected. Spinning up local Spark session.")
        from pyspark.sql import SparkSession
        return SparkSession.builder.master("local[1]").appName("local-tests").getOrCreate()

def get_parameter(key: str, default: str = None) -> str:
    """
    Safely retrieves parameters, degrading gracefully if dbutils is not available (e.g., local IDE).
    """
    try:
        # Attempt to use the Databricks native dbutils 
        from dbruntime.dbutils import DBUtils
        dbutils = DBUtils(my_spark)
        return dbutils.widgets.get(key)
    except (ImportError, Exception):
        # Fallback for local execution (could also check os.environ here)
        print(f"[Local Execution] dbutils unavailable. Defaulting '{key}' to '{default}'")
        return default
