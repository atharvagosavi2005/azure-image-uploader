# Azure Image Uploader

A beginner-friendly Python web app to upload images using Azure Blob Storage and save image metadata in Azure SQL Database.

## 🔧 Azure Services Used

1. **Azure Blob Storage** – Store images
2. **Azure SQL Database** – Save image URLs
3. **Azure App Service** – Host the app
4. **Azure Monitor** – View logs and performance

## 🚀 Features

- Upload image via web UI
- Stores image in Azure Blob
- Saves image URL in Azure SQL
- Monitored with Azure Monitor

## 🧰 Tech Stack

- Python (Flask)
- HTML (form)
- Azure SDK for Python

## ⚙️ Setup Instructions

### 1. Clone Repo

```bash
git clone https://github.com/yourusername/azure-image-uploader.git
cd azure-image-uploader
```

### 2. Install Requirements

```bash
pip install -r requirements.txt
```

### 3. Set Environment Variables

```bash
export AZURE_STORAGE_CONNECTION_STRING="..."
export AZURE_SQL_CONNECTION_STRING="..."
```

### 4. Run App Locally

```bash
python app.py
```

### 5. Deploy to Azure App Service

- Create App Service on Azure
- Deploy via GitHub or ZIP
- Configure environment variables in Azure Portal

## 📷 Screenshot

*(Upload a screenshot of the app UI here)*

## 🧠 Learning Outcome

This project helps you learn how to integrate multiple Azure services into a full-stack project.
