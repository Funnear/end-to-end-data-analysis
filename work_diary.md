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

