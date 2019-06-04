import pandas as pd
import numpy as np

"""Your task is to **find the Pokémon with the best stats, that can best defend the most common type-combination there is.** 
Every Pokémon has either one or two types. In this example, we only care about these with two types (a *type-combination*).   
To solve this task, you first need to find the most common type-combination, which you can do with a groupby on the `Pokemon`-dataset. 
You can save these types as variables, eg. `common_type_1` and `common_type_2`. Then, you can use the `Effectivity_table` to figure 
out the two types which are good defenders against both of these types. To figure these types out, you must select the rows or columns 
which have `0.5` as value for `common_type_1` and `common_type_2`. Note that the table as given here specifies the attacker as rows and 
the defender as columns, so you may want to transpose the table. If you need more information about how the Type-Effectivity-Calculation
 works, take a look at the [Bisafans-Page](https://www.bisafans.de/lexikon/051.php) where the table comes from.      
If you did everything correctly, you will find two types which are good defenders against both `common_type_1` and `common_type_2`. 
Filter the `Pokemon_no_duplicates`-dataset for Pokèmon that have these types (no matter which is Type 1 and which is Type 2), and select 
the one with the highest overall stats (`Total`). You are supposed to return the entire row of the dataset, not only its Name. 
If you did everything correctly, the resulting Pokemon should be **Aggron**."""


def find_best_defender(all_pokemon, effectivity_attack):
    type_nums = all_pokemon.groupby(['Type 1', 'Type 2'])['Name'].count().reset_index()
    type_nums = type_nums.rename({'Name': 'Count'}, axis='columns')
    #merge normal/flying and flying/normal
    common_type_1, common_type_2 =  list(type_nums.iloc[type_nums['Count'].idxmax(axis=0), :][['Type 1', 'Type 2']])
    effectivity_attack = effectivity_attack.fillna('1')
    effectivity_defend = effectivity_attack.T
    defender_type_1, defender_type_2 = list(effectivity_defend[(effectivity_defend[common_type_1] == 0.5) & (effectivity_defend[common_type_2] == 0.5)].index)
    best_defenders = all_pokemon[((all_pokemon['Type 1'] == defender_type_1) & (all_pokemon['Type 2'] == defender_type_2)) | ((all_pokemon['Type 1'] == defender_type_2) & (all_pokemon['Type 2'] == defender_type_1))]
    return best_defenders.sort_values(by='Total', ascending=False).iloc[0]



all_pokemon = pd.read_csv("Pokemon.csv", index_col=0)
effectivity_attack = pd.read_csv("Effectivity_table.csv", index_col=0)
res = find_best_defender(all_pokemon, effectivity_attack)
print(res)
assert type(res) == pd.Series
assert res.to_dict() == {'Name': 'Aggron', 'Type 1': 'Steel', 'Type 2': 'Rock', 'Total': 530, 'HP': 70, 'Attack': 110,
                         'Defense': 180, 'Sp. Atk': 60, 'Sp. Def': 60, 'Speed': 50, 'Generation': 3, 'Legendary': False}