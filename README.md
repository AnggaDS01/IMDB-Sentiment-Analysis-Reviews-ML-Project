# IMDB Sentiment Analysis Reviews ML Project Workflow
---

# Project Workflows
* **constants**
* **config_enity**
* **components**
* **artifact_enity**
* **pipeline**
* **app.py**

# How to run?

## **Step 1: Clone the repository :**

```bash
git clone https://github.com/AnggaDS01/IMDB-Sentiment-Analysis-Reviews-ML-Project.git
```
## **Step 2: Create a virtual environment after opening the repository:**

### Python 3.4 and above
If you are running Python 3.4+, you can use the venv module baked into Python

```bash
# python -m venv <directory>
python -m venv venv
```

### Windows venv activation
To activate your venv on Windows, you need to run a script that gets installed by venv. If you created your venv in a directory called venv, the command would be:

```bash
# In cmd.exe
venv\Scripts\activate.bat
# In PowerShell
venv\Scripts\Activate.ps1
```

### Linux and MacOS venv activation
On Linux and MacOS, we activate our virtual environment with the source command. If you created your venv in the myvenv directory, the command would be:

```bash
$ source myvenv/bin/activate
```

## **Step 3: install the requirements**
```bash
pip install -r requirements.txt
```

## **Step 4: run python app.py in bash**
```bash
# Finally run the following command
python app.py
```
