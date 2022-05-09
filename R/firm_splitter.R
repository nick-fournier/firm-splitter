#### The firm splitter script


### Preliminary declaration ####
#### Added excel tool
library(xlsx)

#### The root folder where the magic happens
# path = 'C:\\gitclones\\firm-splitter\\R'
path = getwd()

#### If there is no output folder, this makes one
if(!dir.exists(file.path(path, 'output')))  dir.create(file.path(path, 'output'))


#### The actual thing ####
#### Reads into the R environment.
# CSV's play nicer, but we can read XLSX with the xlsx function. 
# firms <- read.csv(paste0(path, 'Firm Roster ALL Firms.csv'), check.names = FALSE)

firms <- read.xlsx2(file.path(path, '../All Firm Rosters 05.09.2022.xlsx'), sheetIndex = 1)
colnames(firms) <- gsub('\\.', " ", colnames(firms))


#### Some housekeeping
# remove "." from names, causes some file type issues...
firms[['Firm Name']] <- gsub('\\.', '', firms[['Firm Name']])


# Split col
split_col = 'Firm Sort Name'


#### Split into list of tables by column
firms_split <- split(firms, firms[[split_col]])

#### Save function
lapply(firms_split, function(df) {
  firm_name = unique(df[[split_col]])
  write.xlsx2(df, file.path(path, 'output', paste0(firm_name, '.xlsx')), row.names=FALSE,)
})







