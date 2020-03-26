import pandas as pd

def A() -> pd.DataFrame:
    """
    Citește un fișier cu tab-separated values și îi afișează primele 5 înregistări.

    Returns
    -------
    pandas.DataFrame
        Datele din tsv într-un DataFrame.
    """
    df = pd.read_csv('./chipotle.tsv', sep='\t', header=0)
    print(df.head())
    return df

def B(df:pd.DataFrame):
    """
    Afișează numărul de întregistrări dintr-un DataFrame.

    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame-ul analizat.
    """
    print("\n" + str(len(df.index)) + " înregistrări.\n")
    return

def C(df:pd.DataFrame):
    """
    Execută info() și describe() pe un DataFrame.

    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame-ul analizat.
    """
    print(df.info()) # afișează info despre fiecare câmp (data type, non-null field count)
    print(df.describe()) # statistică: standard deviation, mean, percentile etc.
    return

def D(df:pd.DataFrame):
    """
    Afișează numele coloanelor.

    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame-ul analizat.
    """
    col_list = df.columns.tolist()
    print('\nColoane: ', col_list)
    print('Număr coloane: ', len(col_list))
    return

def E():
    print("\nDacă nu se specifică o coloană, indexarea se face începând de la 0, prin incrementare, deci va avea valori unice.")
    print("Dacă se specifică una, indexul fiecărei linii este valoarea de pe coloană a liniei respective.")
    print("Exemplu: df.set_index('Something')")
    print("Astfel, indexul nu este neapărat o valoare unică; condiție care se verifică cu pandas.Index.is_unique.")
    return

def F(df:pd.DataFrame):
    """
    Afișează mărfurile vândute și numărul lor.
    
    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame-ul analizat.
    """
    products = df['item_name'].unique()
    print("\nProduse: ", products)
    print("Nr. produse: ", len(products))
    return

def G(df:pd.DataFrame):
    """
    Afișează numărul de obiecte comandate.
    
    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame-ul analizat.
    """
    print("\nNr. produse comandate: ", df["quantity"].sum())
    return

def H(df:pd.DataFrame):
    """
    Afișează statistici despre vânzarea produsului 'Chicken Crispy Tacos'.

    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame-ul analizat.
    """
    df2 = df.copy()
    df2[['item_price']] = df2[['item_price']].apply(lambda x: x.str.replace('$','')).apply(pd.to_numeric)
    df2 = df2[df2['item_name'] == 'Chicken Crispy Tacos']
    cct_stats = df2.describe()
    print("\nStatistici Chicken Crispy Tacos: \n\n", cct_stats)
    print("\nPreț minim: ", cct_stats['item_price']['min'])
    print("Preț maxim: ", cct_stats['item_price']['max'])
    print("Preț mediu: ", round(cct_stats['item_price']['mean'], 2))
    print("Preț median: ", df2['item_price'].median())
    print("Număr de produse: ", int(cct_stats['quantity']['count']))
    print("Total venituri: ", df2["item_price"].sum())
    return

def I(df:pd.DataFrame):
    """
    Afișează cele mai comandate trei mărfuri.

    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame-ul analizat.
    """
    quantities = df.groupby('item_name')['quantity'].sum()
    print("\nCele mai comandate trei mărfuri: ", quantities.nlargest(3).index.tolist())
    return

def J(df:pd.DataFrame):
    """
    Afișează de câte ori s-a comandat 'Veggie Salad Bowl'.

    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame-ul analizat.
    """
    print('\nComenzi de Veggie Salad Bowl:', df.groupby(['item_name'])['item_name'].count()['Veggie Salad Bowl'])
    return

def K(df:pd.DataFrame):
    """
    Afișează în câte comenzi s-au cerut mai multe Canned Sodas.

    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame-ul analizat.
    """
    df_cs = df.loc[(df['item_name']=='Canned Soda') & (df['quantity'] > 1)]
    print('\nNr. comenzi cu mai multe Canned Sodas:', len(df_cs))
    return

def L(df:pd.DataFrame):
    """
    Afișează sumele încasate pentru fiecare comandă.

    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame-ul analizat.
    """
    df[['item_price']] = df[['item_price']].apply(lambda x: x.str.replace('$','')).apply(pd.to_numeric)
    df['total_price'] = df['item_price'] * df['quantity']
    df_agr = df.groupby(['order_id'])['total_price'].sum()
    print('\nÎncasări pentru fiecare comandă:\n', df_agr)
    return

if __name__ == "__main__":
    df = A()
    B(df)
    C(df)
    D(df)
    E()
    F(df)
    G(df)
    H(df)
    I(df)
    J(df)
    K(df)
    L(df)