import pandas as pd
df = df[df['str_type'].map(lambda x: x[:2] in ['03'])]
