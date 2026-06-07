# Datasets

The notebooks run on a **customer churn** example. 

Datasets are **not committed** - `data/` is gitignored. Obtain your own copy as follows.

## IBM Telco Customer Churn

- 7,043 customers, 21 columns: demographics, services, contract, `MonthlyCharges` / `TotalCharges`, `tenure`, and a `Churn` label.
- Public sample dataset, widely used as the canonical churn benchmark.
- Source: https://github.com/IBM/telco-customer-churn-on-icp4d (also mirrored on Kaggle).

### Download locally

Expected path: `data/telco_customer_churn.csv`.

PowerShell:

```powershell
Invoke-WebRequest `
  -Uri "https://raw.githubusercontent.com/IBM/telco-customer-churn-on-icp4d/master/data/Telco-Customer-Churn.csv" `
  -OutFile "data/telco_customer_churn.csv"
```

bash / curl:

```bash
curl -L -o data/telco_customer_churn.csv \
  https://raw.githubusercontent.com/IBM/telco-customer-churn-on-icp4d/master/data/Telco-Customer-Churn.csv
```

### Copy into Databricks

The notebooks read the real data from a Unity Catalog Volume. Create the Volume once, then upload the file:

```sql
CREATE VOLUME IF NOT EXISTS <catalog>.<schema>.raw;
```

```bash
databricks fs cp data/telco_customer_churn.csv \
  dbfs:/Volumes/<catalog>/<schema>/raw/telco_customer_churn.csv
```

Point the notebook's loader at `/Volumes/<catalog>/<schema>/raw/telco_customer_churn.csv`. 