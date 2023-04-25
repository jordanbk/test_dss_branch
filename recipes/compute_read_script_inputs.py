# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu
import io

# Read recipe inputs
script_inputs = dataiku.Folder("e4onN8Hu")
script_inputs_info = script_inputs.get_info()

#print(folder.list_paths_in_partition()) -- double-check the filename
with script_inputs.get_download_stream("/orders.csv/orders.csv") as f:
    data = f.read()
#print(data)
#df = pd.read_csv(io.StringIO(data.decode('utf-8')))

# Compute recipe outputs
# TODO: Write here your actual code that computes the outputs
# NB: DSS supports several kinds of APIs for reading and writing data. Please see doc.

read_script_inputs_df = df


# Write recipe outputs
read_script_inputs = dataiku.Dataset("read_script_inputs")
read_script_inputs.write_with_schema(read_script_inputs_df)
