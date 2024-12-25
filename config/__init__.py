from dotenv import load_dotenv
from os import getenv
load_dotenv()

NAME = "Ecoi"
DATABASE = {
    "connectionString": "mongodb://localhost:27017/",
    "dbName": "EcoiDB"
}
GA4 = {
    "API_SECRET": getenv("GA4_API_SECRET"),
    "MEASUREMENT_ID": getenv("GA4_MEASUREMENT_ID")
}