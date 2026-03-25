# NSEE-IMT Internship Challenge: Data Science & AI

This repository contains the solution for the Data Science technical challenge proposed by the **Núcleo de Sistemas Eletrônicos Embarcados (NSEE)** at **Instituto Mauá de Tecnologia (IMT)**. 

The project implements a complete Python pipeline for cleaning, processing, and pre-processing the São Paulo Cancer Hospital Registry (RHC/SP) database, structuring it mathematically and making it ready for *Machine Learning* model training.

## 📁 Repository Structure

* **`Desafio.py`**: Main script containing all the data filtering, feature engineering, and pre-processing code.
* **`Justificativa.md`**: Document containing the technical defense of the analytical decisions made (e.g., handling null values, dropping identifiers, and applying *One-Hot Encoding*).
* **`Desafio_de_Estágio-1.pdf`**: Original file containing the instructions and business rules required for the project scope.
* **`requirements.txt`**: List of libraries and dependencies needed to run the code.

## 🛠️ Tech Stack
* **Python 3.14.2**
* **Pandas** and **NumPy**
* **dbfread**

## 🚀 How to Run the Project

Follow the step-by-step instructions below in your terminal to set up the environment and run the script locally. 

> **⚠️ Warning:** Due to the large size of the dataset and in strict compliance with the Brazilian General Data Protection Law (**LGPD**), the raw `.dbf` database containing medical records has not been included in this repository. Please make sure to download the public RHC/SP database and place it in the root folder of the project before running the script.

**1. Create the virtual environment:**
```bash
py -m venv venv
```

**2. Activate the virtual environment:**
```bash
venv\Scripts\activate
```

**3. Install the dependencies:**
```bash
pip install -r requirements.txt
```

**4. Run the main script:**
```bash
py Desafio.py
```

## ⚖️ License
This project was developed for technical assessment purposes for the Instituto Mauá de Tecnologia.
