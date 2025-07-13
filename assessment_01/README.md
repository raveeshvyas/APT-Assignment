# Files in this directory
1. `mapping.json`: Mapping the given columns to actual ones, with confidence scores
2. `analysis.ipynb`: Analysis of the dataset, along with justification
3. `validate_mapping.py`: Validates the integrity of our mapping
4. `thought_process.md`: Our thought process while approaching this problem

# Running the scripts
* Copy the data file `02_sample_data_with_fabricated_columns.csv` into this directory
* Create a virtual environment, if required
* Install the dependencies
```bash
python3 -m venv env
source venv/bin/activate # on Linux

pip install -r requirements.txt
```
### `analysis.ipynb`
* Simply run the python notebook
### `validate_mapping.py`
* Ensure `mapping.json` is present in this directory
* Simply run the script