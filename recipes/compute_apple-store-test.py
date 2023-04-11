# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
AppleStore = dataiku.Dataset("AppleStore")
AppleStore_df = AppleStore.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

apple_store_test_df = AppleStore_df # For this sample code, simply copy input to output


# Write recipe outputs
apple_store_test = dataiku.Dataset("apple-store-test")
apple_store_test.write_with_schema(apple_store_test_df)
