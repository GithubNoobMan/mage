if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    """
    Template code for a transformer block.

    Add more parameters to this function if this block has multiple parent blocks.
    There should be one parameter for each output variable from each parent block.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    import datetime as dt 
    import pandas as pd
    import re
    print(data.columns)
    #Remove rows
    data = data.loc[(data.passenger_count > 0) & (data.trip_distance > 0)]

    #lpep_pickupdate
    data['lpep_pickup_date'] = pd.to_datetime(data.lpep_pickup_datetime).dt.date

    def insert_underscore(text):
        return re.sub(r'([a-z])([A-Z])', r'\1_\2', text)

    #Lower the columns

    data.columns = [insert_underscore(col) for col in data.columns]
    data.columns = data.columns.str.lower()

    return data


@test
def test_output(data, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert data is not None, 'The output is undefined'
    assert data[data.passenger_count == 0].empty, 'Passenger Count not 0'
    assert data[data.trip_distance == 0].empty, 'Passenger Count not 0'
    assert 'vendor_id' in data.columns, 'Columns not snake case'
