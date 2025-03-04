## Developer setup

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

