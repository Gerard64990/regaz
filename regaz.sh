#!/bin/bash

year=$(date +"%Y")
month=$(date +"%m")

datefile="gaz_0"$month$year
if [ $month -ge 10 ]
then
    datefile="gaz_"$month$year
fi
echo "Curl"
curl --silent -X POST "https://www.myregaz.com/api-public/consumption/ID_TO_REPLACE/statistics/xls" --data "month="$month"&year="$year --output $datefile".xlsx" > /dev/null

echo "Call xlsx2csv.py"
/xlsx2csv.py $datefile
rm $datefile.xlsx

numlines=$(cat $datefile.csv | wc -l)
if [ $numlines -gt 2 ]
then
    echo "OK, num record:"$numlines". Call sendGasToInflux.py"
    /sendGasToInflux.py $datefile.csv
else
    echo "KO"
fi
