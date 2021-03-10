# Innovationstag 2021: How to survive tv series?
This sample provides a jupyter notebook which was also demonstrated on Google Colab. If you particpated in our innovation day workshop you've received a share link on Colab as well. If you did not participate or you do not want to use Colab, than you may use this repository to execute the notebook locally.

## Prerequisites
You need to have Python and Jupyter Lab on your notebook. 

- [Python](https://www.python.org/) 
- [Jupyter](https://jupyter.org/)
- Python libraries: scrapy, pandas, seaborn and sklearn (see virtual environment)

Depending on your installation, all necessary tools may also be installed from your development environment. For the libraries, you may just install them from within the notebook or install them based on the provided requirements file (as described in next section).

## Usage
You may install all requirements globally. However, it is recommendedIn this folder, create a virtual environment. To so on Windows call from your commandline (PowerShell or CMD):
 ```Powershell
py -3 -m venv .venv
.venv\scripts\activate
 ```
 To create a virtual environment on Linux or MacOs:
```bash 
pip3 install -r ./requirements.txt
```
 python3 -m venv .venv
source .venv/bin/activate

### Install Dependencies
Now you may install all necessary libs.
```bash 
pip3 install -r ./requirements.txt
```

### VS Code
A very convinient way to set-up Python with Jupyter is using [Visual Studio Code](https://code.visualstudio.com/). There is also an excellent [introduction](https://code.visualstudio.com/docs/python/python-tutorial) to VS Code and Python and a special section on how to use [notebooks](https://code.visualstudio.com/docs/python/jupyter-support). If you choose VS Code simply open this folder with it and double click the `walking_dead.ipynb` file to start working with our notebook.

If you created a virtual environment you need to activate this in VS Code. The IDE should present a prompt to do so, if you followed the instructions [above](Usage).

## Remarks
As said in our workshop and outlined in the notebook, the underlying data which we scraped from the web is not really a good data set and this will also be obvious in prediction results.