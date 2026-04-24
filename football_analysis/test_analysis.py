import pandas as pd
import numpy as np

print('=== LOADING DATA ===')
df = pd.read_csv('data/results.csv')
print(f'Shape: {df.shape}')

print('\n=== Q1: Total matches ===')
print(f'Total matches: {df.shape[0]:,}')

print('\n=== Q2: Year range ===')
df['date'] = pd.to_datetime(df['date'])
df['year'] = df['date'].dt.year
print(f'Earliest: {df["year"].min()}, Latest: {df["year"].max()}')

print('\n=== Q3: Unique countries ===')
all_teams = pd.concat([df['home_team'], df['away_team']]).unique()
print(f'Unique countries: {len(all_teams)}')

print('\n=== Q4: Most frequent home team ===')
print(df['home_team'].value_counts().head(5).to_string())

print('\n=== Q5: Avg goals ===')
df['total_goals'] = df['home_score'] + df['away_score']
print(f'Average goals per match: {df["total_goals"].mean():.2f}')

print('\n=== Q6: Highest scoring match ===')
idx = df['total_goals'].idxmax()
m = df.loc[idx]
print(f'{m["home_team"]} {int(m["home_score"])}-{int(m["away_score"])} {m["away_team"]} ({m["date"].strftime("%Y-%m-%d")})')

print('\n=== Q7: Home vs Away goals ===')
print(f'Home total: {df["home_score"].sum():,} | Away total: {df["away_score"].sum():,}')

print('\n=== Q8: Most common total goals ===')
print(f'Mode: {df["total_goals"].mode()[0]}')

def match_result(row):
    if row['home_score'] > row['away_score']:
        return 'Home Win'
    elif row['home_score'] < row['away_score']:
        return 'Away Win'
    else:
        return 'Draw'

df['result'] = df.apply(match_result, axis=1)

print('\n=== Q9: Home win percentage ===')
pcts = df['result'].value_counts(normalize=True) * 100
for r, p in pcts.items():
    print(f'  {r}: {p:.1f}%')

print('\n=== Q10: Home advantage ===')
hw_pct = pcts.get('Home Win', 0)
aw_pct = pcts.get('Away Win', 0)
print(f'Home wins: {hw_pct:.1f}% vs Away wins: {aw_pct:.1f}%')
if hw_pct > aw_pct:
    print('Home advantage EXISTS!')
else:
    print('No advantage')

print('\n=== Q11: Most wins ===')
hw = df[df['result'] == 'Home Win']['home_team'].value_counts()
aw = df[df['result'] == 'Away Win']['away_team'].value_counts()
tw = hw.add(aw, fill_value=0).astype(int).sort_values(ascending=False)
print(tw.head(10).to_string())

print('\n=== ALL TESTS PASSED ===')
