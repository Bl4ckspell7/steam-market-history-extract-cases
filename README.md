# CS2 Market History - Case Data Extractor
A Python script that filters and organizes Counter-Strike 2 market history data from a CSV file. It extracts all case-related trade entries and saves each unique case to its own clean, individual CSV file for easier analysis or tracking.

## Example
### Input
`market_data.csv`
```csv
Item Name,Game Name,Listed On,Acted On, Display Price, Price in Cents, Type, Market Name, App Id, Context Id, Asset Id, Instance Id, Class Id, Unowned Context Id, Unowned Id
"Spectrum Case","Counter-Strike 2","1 Apr","1 Apr","0,08€","8","purchase","Spectrum Case","730","2","39812736482","0","9032857146","2","39812736482"
"Spectrum Case","Counter-Strike 2","1 Apr","1 Apr","0,08€","8","purchase","Spectrum Case","730","2","62583921074","0","1830295712","2","62583921074"
"Spectrum Case","Counter-Strike 2","1 Apr","1 Apr","0,08€","8","purchase","Spectrum Case","730","2","93472138572","0","7261058493","2","93472138572"
"Spectrum Case","Counter-Strike 2","1 Apr","1 Apr","0,08€","8","purchase","Spectrum Case","730","2","17845392016","0","3182594105","2","17845392016"
"Danger Zone Case","Counter-Strike 2","1 Apr","1 Apr","0,05€","5","purchase","Danger Zone Case","730","2","64918237501","0","4592763845","2","64918237501"
"Danger Zone Case","Counter-Strike 2","1 Apr","1 Apr","0,05€","5","purchase","Danger Zone Case","730","2","23897461529","0","5914720934","2","23897461529"
"Danger Zone Case","Counter-Strike 2","1 Apr","1 Apr","0,05€","5","purchase","Danger Zone Case","730","2","15739648126","0","3701826391","2","15739648126"
```
### Output
`cases_output/Danger Zone Case.csv`
```csv
Item Name,Listed On,Acted On,Display Price,Type
Danger Zone Case,1 Apr,1 Apr,"0,05€",purchase
Danger Zone Case,1 Apr,1 Apr,"0,05€",purchase
Danger Zone Case,1 Apr,1 Apr,"0,05€",purchase
```
`cases_output/Spectrum Case.csv`
```csv
Item Name,Listed On,Acted On,Display Price,Type
Spectrum Case,1 Apr,1 Apr,"0,08€",purchase
Spectrum Case,1 Apr,1 Apr,"0,08€",purchase
Spectrum Case,1 Apr,1 Apr,"0,08€",purchase
Spectrum Case,1 Apr,1 Apr,"0,08€",purchase
```
