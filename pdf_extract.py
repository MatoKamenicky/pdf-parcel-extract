import pymupdf
import pandas as pd
import os

def input_files(input_folder):
    file_paths = []
    files = []
    for file in os.listdir(input_folder):
        file_path = os.path.join(input_folder, file)
        if os.path.isfile(file_path):
            file_paths.append(file_path)
            files.append(file)
    return files, file_paths


def output_files(output_folder, file_name):
    file_name = f"parcel_numbers_{file_name}.txt"
    file_path = os.path.join(output_folder, file_name)
    return file_path


def find_tables(doc):
    all_tabs = []
    for page in doc:
        tabs = page.find_tables(strategy="lines_strict")
        for tab in tabs:
            if tabs.tables:
                df = tab.to_pandas(header_rows=None)
                if not all_tabs:
                    all_tabs.append(df)
                elif all_tabs[0].columns.equals(df.columns):
                    all_tabs.append(df)
                else:
                    current_header_row = pd.DataFrame([df.columns], columns=list(all_tabs[0].columns))
                    df.columns = list(all_tabs[0].columns)
                    df = pd.concat([current_header_row, df], ignore_index=True)
                    all_tabs.append(df)

    combined_df = pd.concat(all_tabs, ignore_index=True)
    combined_df.replace('', None, inplace=True)
    df_cleaned = combined_df.dropna(subset=["Číslo\nparcely"])
    return df_cleaned



def table_to_txt(df, file_path):
    parcel_numbers = df["Číslo\nparcely"]
    i = 0
    with open(file_path, "w", encoding="utf-8") as file:
        for number in parcel_numbers:
            i += 1
            if i == 1:
                file.write("(\n")
            if i == len(parcel_numbers):
                file.write(f'"ParcelNumber" = \'{number}\'\n')
                file.write(") and\n\"OriginalCuValue\" != 1")
            else:
                file.write(f'"ParcelNumber" = \'{number}\' or\n')


if __name__ == "__main__":
    input_folder = os.path.join(os.getcwd(), "input_data")
    output_folder = os.path.join(os.getcwd(), "output_data")

    files, file_paths = input_files(input_folder)
    for file, file_path in zip(files, file_paths):
        print(file)
        doc = pymupdf.open(file_path)
        df = find_tables(doc)
        file_path = output_files(output_folder, file)
        table_to_txt(df, file_path)

    
    