"""Import the QA questions for automated processing."""
import json
import pandas as pd

def import_questions(filepath):
    """Import the questions from a .json file and return a dictionary of dataframes."""
    
    if _check_json_filepath(filepath):
        with open(filepath) as f:
            data = json.load(f)

        # For each key of data, create a pandas dataframe with its values
        dataframes = {}
        for key in data:
          # Create variable name based on key
          dataframes[key] = pd.DataFrame(data[key])

        return dataframes

def _check_json_filepath(filepath):
    if not filepath:
        raise ValueError('Filepath must be provided')
    
    if filepath == '':
        raise ValueError('Filepath must be provided')

    if not filepath.endswith('.json'):
        raise ValueError('Filepath must be a .json file')

    return True