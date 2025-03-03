# End-to-End Data Analytics Project
IronHack Data Science / Machine Learning bootcamp: individual project on End-to-End Data Analysis.


## Objective
A data project lifecycle consists of multiple interconnected phases, spanning from data cleaning and exploration to advanced analysis and reporting.
In this project, you will experience the end-to-end process of performing a comprehensive data analysis.

By combining the strengths of Python for data manipulation and exploration, you will gain a deeper understanding of how these tools complement each other in real-world scenarios.

The objective is not only to answer business questions but also to critically engage with the data—cleaning, structuring, exploring patterns, and visualizing findings before translating them into actionable insights.

## Requirements

1. Pick a topic and choose a dataset.
2. *Data Analysis*: Understand your dataset and create a report (e.g., Word document) summarizing it.
3. *Data Exploration and Business Understanding*.

*Bonus Points*
- Augment your data with web scraping.
- Include visualizations from Python and/or Tableau in the final presentation.
- Apply statistical tests like Chi-Square or others if they make sense.
- Automate tasks with Python scripts, such as cleaning steps.
- Add a dashboard for data visualization.
- Use SQL to create a database with your data.

*Mandatory Deliverables*
1. Presentation: 8–15 minutes per person.
2. Python Code: Well-documented Python script covering:
- At least one use of lambda, apply...
- At least two groupby operations and aggregations.
- At least one frequency table.
3. Visualization:
- Minimum of three plots
- showcasing univariate and multivariate analysis
- bonus to do it also in Tableau dashboard
4. README File: A comprehensive README explaining the project, dataset, methodology, and results.

----

# <Placeholder: topic of research>

<Placeholder: business context of the research.>

## Dataset description

### Source:

### Fields:

## Methodology

## Results

---

## Extra materials
- [Link to the presentation slides](about:blank)
- extrnal articles?

---

## Installation

To run this project locally, follow these instructions:

1. **Clone the repo:**

```bash
git clone https://github.com/Funnear/end-to-end-data-analysis
```

2. **Virtual environment:**

Create the virtual environment: 
```bash
python3 -m venv venv
```

Activate the virtual environment:

- For Windows: 
```bash
venv\Scripts\activate
```

- For Linux/Mac: 
```bash
source venv/bin/activate
```

To switch back to normal terminal usage or activate another virtual environment to work with another project run:
```deactivate```

3. **Install dependencies:**

```bash
pip install --upgrade pip; \
pip install -r requirements.txt
```

4. Configure using the same environment for Jupyter Notebooks

After running this comand in terminal:
```bash
python -m ipykernel install --user --name=venv --display-name "Python (venv)"
```
restart VS code.
Open a `.ipynb` file and add code block at the top with:
```python
!which python
```
Try running the cell. VS Code will prompt for choosing a Jupyter kernel:
- Select another kernel
- Jupyter kernel
- Refresh the list using icon on the top right!
- Choose the virtual environment of this project.

Run the code cell again and make sure it returns the correct path to `<this project folder>/venv/bin/python3`

This will resolve all possible `ModuleNotFoundError` occurences when importing libraries.

