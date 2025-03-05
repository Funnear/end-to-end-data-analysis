#### Brainstorming
```bash
git checkout brainstorming
```

In the separate branch I have created a notebook to overview the data sets that Chat GPT has recommended for me based on my prompt:
> I am looking for a topic for data analysis. I can only choose datasets from public resources like: Kaggle, Machine Learning Repository, PorData and any other.
> I want my research to be about Entertainment and EDM scene. 
> It can be about music labels and releases for some specific genres. Or about artist bookings on festivals and their target audiences. Information about social media engagement for artists and labels is also interesting to study. And information about music distribution, music streaming and vinyl sales is interesting.
> Can you help me to find relevant data within the public access?

#### Virutal Environment

It is convenient to use the same virtual environment for the python script as for Jupyter Notebooks inside the same project. But activating venv (or other alias for virtual environment) doesn't automatically set Python kernel path for the GUI app that is used for working with Jupyter Notebooks.

In the documnetation to this project under the Installation header the approach for using the same path for notebooks as for scripts is described. `ipykernel` is the library that is required for VS Code integration, it is installed together with `jupyterlab`.

This way it can be ensured that all libraries are installed seamlessly and there will be no conflicts of versions.

#### Big Data from Kaggle

The datasets that interest me are bulky. Github is not designed for storing big files, only for code sources. Access to data raw source via URL is not always possibel as it requires authentication, for instance on Kaggle.

Kaggle provides internal tools for using the datasets from this platform. Sample code:

```python
# Install dependencies as needed:
# pip install kagglehub[pandas-datasets]
import kagglehub
from kagglehub import KaggleDatasetAdapter

# Set the path to the file you'd like to load
file_path = "discogs_20250101_artists.csv"

# Load the latest version
df = kagglehub.load_dataset(
  KaggleDatasetAdapter.PANDAS,
  "ofurkancoban/discogs-datasets-january-2025",
  file_path,
  # Provide any additional arguments like 
  # sql_query or pandas_kwargs. See the 
  # documenation for more information:
  # https://github.com/Kaggle/kagglehub/blob/main/README.md#kaggledatasetadapterpandas
)

print("First 5 records:", df.head())
```

#### Kaggle API

Using Kaggle API requires authentication, but there are automated methods of getting access to the data using API keys:
[https://www.kaggle.com/docs/api#authentication](https://www.kaggle.com/docs/api#authentication)

In the example above loading dataset from Kaggle server didn't require me to provide authentication tockens. 

However, setting up API tocken and installing Kaggle CLI tool opens a door to lookup for data sets from terminal:

```bash
pip install kaggle; \
kaggle datasets list -s my_keyword
```

This way I have found and downloaded an extra data sets that might be useful:
```bash
kaggle datasets download -d mrmorj/dataset-of-songs-in-spotify; \
kaggle datasets download -d mathurinache/1000000-bandcamp-sales; \
kaggle datasets download -d bvitos/electronic-music-features-202101-beatporttop100
```

#### using custom python code in notebooks

For troubleshooting. Exucute this Python code from a root directory of the project:
```python
import sys
import os

sys.path.append(os.path.abspath(".")) 
print("sys.path:", sys.path)
```

TODO: add this later to README.md:
``` bash
pip install -e .
```
the path should be to the folder that contains setup.py

setup.py must list folders containing `__init__.py` files.

Contents of package folders can be used in Python and Jupyter files:
```python
from src import eda
```

#### Dataset pack for data frame maintenance

Created module src/datasets to automate reading and writing dataframes to/from files and keeping them in a dictionary for repeated actions.
It required usage of Python classes, `os` module for generating paths, and stream reading / writing for files.

##### How it works

0. :warning: [ Under construction] Import data sets from Kaggle directly and automatically and store as csv files locally, without using github repo for this.

1. Import the data sets from csv files for the first time.

To quickly get file names of datasets in the code copy output from terminal:
```bash
cd datasets; ls -1
```
And then use multicoursor editing feature.

```python
from src import eda, datasets

datasets_files = [
'1000000-bandcamp-sales.csv', 
'discogs_20250101_artists.csv', 
'release_data.csv']

project_pack = datasets.DatasetPack()

dataset1 = datasets.Dataset('df_bandcamp_sales', datasets_files[0])
project_pack.add_dataset(dataset1)

dataset2 = datasets.Dataset('df_discogs_artists', datasets_files[1])
project_pack.add_dataset(dataset2)

dataset3 = datasets.Dataset('df_discogs_releases', datasets_files[2])
project_pack.add_dataset(dataset3)
```
- this code runs for 14.4 seconds for this project on developer's workstation.

2. Regular usage

Now if I want to work with my dataframe inside the notebook, not from the python modules, I can do this:
```bash
df_bandcamp_sales = project_pack.dictionary['df_bandcamp_sales'].dataframe.copy()
```

But ideally I want to cycle throught the dataset pack and repeat the same code for every dataset:
```python
for label, dataset in project_pack.dictionary.items():
    print(f"================= {label} =================")
    dataset.dataframe.info()
    print()
```

3. Backup

3.1 Save all dataframes to pickles

```python
for _, dataset in project_pack.dictionary.items():
    dataset.backup()
```

3.2 Save pack information as json file
```python
project_pack.backup_pack()
```

4. Restore

Next time I open a Jupyter notebook I can pick up from where I left off without running all code again.
It is useful when I have several notebooks for different project stages:
```python
project_pack = datasets.DatasetPack(restore=True)
```
- before cleanup, this code runs for 2.5 seconds for this project on developer's workstation.
- after cleanup, this code runs for ??? seconds for this project on developer's workstation.

#### Using logger for debugging purposes

Put this code in Jupyter notebook somewhere at the top:
```python
import logging
logging.getLogger().setLevel(logging.DEBUG)
```

Other levels:
- DEBUG - what developers look at
- INFO - extra information on what's happening
- WARNING - this won't stop your code from running but you're doing something slightly off
- EXCEPTION / ERROR - this will stop your code but you'll get extra info on the error

Put this code in Jupyter notebook or Python script:
```python
logging.debug(f"The age ({age}) is between 24 and 34")
```

