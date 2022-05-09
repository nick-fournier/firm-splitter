# Firm Splitter
## Split excel file into separate files or sheets by a single column group (i.e., group-by-column)


### How to use it?

1. Move/create a firm_splitter_settings.txt file in the same folder as the firm_splitter.exe
2. Open the `firm_splitter_settings.txt` file and enter your settings for each parameter, like so:
```
  input_file: some_excel_file.xlsx
  input_sheet: SheetName
  output_folder: your_output_folder
  split_column: Firm Sort Name
  separate_files: True
```
3. Double click the firm_splitter.exe file and voila!


The firm_splitter_settings.txt *must* be in the same folder as the firm_splitter.exe file, but you can specify an xlsx file and output folder anywhere on your computer.

- input_sheet is optional if your excel workbook only has one sheet
- split_column is the column name in the excel file
- separate_files can be True or False, and specifies whether to create separate files for each group, or as sheets in one workbook

