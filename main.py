from galvani import BioLogic
import pandas as pd
import click
import csv
import os

'''
This program reads the ".mpeg" files and interleaves them according to the
time column. The resulting file will be a ".CSV"
'''


@click.command()
@click.argument('file1', type=click.Path(exists=True))
@click.argument('file2', type=click.Path(exists=True))
@click.option('--dst', default="resul.csv")
def lectorDeArchivosMPR(file1, file2, dst):
    mpr_file = BioLogic.MPRfile(file1)
    df1 = pd.DataFrame(mpr_file.data)
    vdf1 = df1.to_numpy()
    colums1 = df1.columns.tolist()

    mpr_file = BioLogic.MPRfile(file2)
    df2 = pd.DataFrame(mpr_file.data)
    vdf2 = df2.to_numpy()

    dst = extension_csv(dst)

    if os.path.isfile(dst):
        os.remove(dst)

    with open(dst, 'a', newline='') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_NONNUMERIC)
        wr.writerow(colums1)
        i = 0
        j = 0
        len1 = len(df1)
        len2 = len(df2)

        while i < len1 and j < len2:
            if vdf1[i][2] < vdf2[j][2]:
                wr.writerow(vdf1[i])
                i += 1
            elif vdf1[i][2] > vdf2[j][2]:
                wr.writerow(vdf2[j])
                j += 1
            else:
                wr.writerow(vdf1[i])
                i += 1
                j += 1

        while i < len1:
            wr.writerow(vdf1[i])
            i += 1

        while j < len2:
            wr.writerow(vdf2[j])
            j += 1


def extension_csv(file):
    parts = file.split(".")
    if parts[len(parts)-1] == "csv":
        return file
    else:
        return file+".csv"


if __name__ == '__main__':
    lectorDeArchivosMPR()
