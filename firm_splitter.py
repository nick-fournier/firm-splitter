import os
import pandas as pd


def firm_splitter():
    print("Welcome to firm splitter! Let's go!!!")

    # Get settings from txt file
    with open('firm_splitter_settings.txt', 'r') as f:
        settings = dict(i.strip().split(':', 1) for i in f)
    settings = {k: v.strip() for (k, v) in settings.items()}

    # Check boolean separate files or not
    settings['separate_files'] = settings.get('separate_files', False)
    if isinstance(settings['separate_files'], str):
        settings['separate_files'] = bool(settings['separate_files'].lower())

    # Load workbook
    try:
        workbook = pd.read_excel(settings['input_file'], sheet_name=settings.get('input_sheet'))
    except:
        print("Couldn't find the input file specified :(")

    # If sheet not specified and only contains one sheet, turn into data frame
    if len(workbook) == 1 and isinstance(workbook, dict):
        workbook = list(workbook.values()).pop()

    # Check if output folder exists
    if not os.path.exists(settings['output_folder']):
        os.mkdir(settings['output_folder'])

    # Check if split column exists
    if settings.get('split_column') not in workbook.columns:
        print('Split columns: '  + settings.get('split_column') + ' not found in the sheet!')
        raise


    # Split the data and save
    if settings['separate_files']:
        for name, firm_df in workbook.groupby(settings.get('split_column')):
            firm_df.to_excel(os.path.join(settings['output_folder'], name + '.xlsx'))
            print('Just split: ' + name)
    else:
        fname = os.path.join(settings['output_folder'], os.path.splitext(settings['input_file'])[0] + '_split.xlsx')
        with pd.ExcelWriter(fname) as writer:
            for name, firm_df in workbook.groupby(settings.get('split_column')):
                firm_df.to_excel(writer, sheet_name=name)
                print('Just split: ' + name)

    print("DONE!!! Hooray!")


if __name__ == "__main__":
    firm_splitter()
