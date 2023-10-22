import pandas as pd

if __name__=="__main__":
    arrets_lignes = pd.read_csv("data/arrets-lignes.csv", sep=";")
    print(arrets_lignes.head())