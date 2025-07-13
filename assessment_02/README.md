# Files in this directory
1. `timeline_visualization.ipynb`: Script to visualize the timeline of workers
2. `duplication_analysis.csv`: CSV containing analysis of the duplicate values
3. `dup_script.ipynb`: Script used to generate the above
4. `deduplicate.py`: Script to generate the deduplicated CSV file
5. `future_improvements.md`: Points about how to prevent race conditions

# Running the scripts
* Copy the data files `03_worker_logs.csv` and `04_final_output.csv` into this directory
* Create a virtual environment, if required
* Install the dependencies
```bash
python3 -m venv env
source venv/bin/activate # on Linux

pip install -r requirements.txt
```
### `timeline_visualization.ipynb`
* Simply run the python notebook
### `deduplication.py`
* Run the script along with the following command line arguments
    1. Input csv file
    2. Output csv file
    3. Method: `last`, `average` or `highest`


