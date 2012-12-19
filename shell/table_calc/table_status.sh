#!/bin/sh
#nt=`hadoop fs -ls /app/ns/udw/release/warehouse` 
#echo $nt > `awk '{print $7}'`

#echo $nt
hadoop=~/lib/hadoop/bin/hadoop
 ${hadoop} fs -ls /app/ns/udw/release/warehouse | awk '{print $8}' | awk -F/ '{print $7}' > tables.txt 
cat tables.txt | while read table 
do
	#echo $table
	  ${hadoop} fs -dus /app/ns/udw/release/warehouse/${table}/*/event_day=20121218 | awk -F/ '{print $9,$NF}'|awk '{print $1," ", $3}' 
done
