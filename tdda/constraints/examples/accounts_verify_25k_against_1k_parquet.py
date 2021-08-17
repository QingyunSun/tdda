# accounts_verify_25k_against_1k_parquet.py

from __future__ import print_function

from tdda.constraints.pd.constraints import verify_df, load_df

df = load_df('testdata/accounts25k.parquet')
verification = verify_df(df, 'testdata/accounts1k.tdda')

print('Basic Verification:')
print(verification)
print('\n')
print('Verification DataFrame:')
dfv = verification.to_frame()
print(dfv)

