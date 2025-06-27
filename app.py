from flask import Flask, request, render_template
from azure.storage.blob import BlobServiceClient
import pyodbc
import os
import logging

app = Flask(__name__)

# Azure Blob setup
connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
blob_service_client = BlobServiceClient.from_connection_string(connect_str)
container_name = "images"

# Azure SQL setup
conn = pyodbc.connect(os.getenv('AZURE_SQL_CONNECTION_STRING'))
cursor = conn.cursor()

@app.route("/", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        image = request.files["image"]
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=image.filename)
        blob_client.upload_blob(image, overwrite=True)

        image_url = f"https://<your_storage_account>.blob.core.windows.net/{container_name}/{image.filename}"
        cursor.execute("INSERT INTO Images (url) VALUES (?)", (image_url,))
        conn.commit()

        logging.info(f"Image uploaded: {image_url}")
        return f"Image uploaded: <a href='{image_url}'>{image_url}</a>"
    return render_template("index.html")
