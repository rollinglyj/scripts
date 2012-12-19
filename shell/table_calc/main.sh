#!/bin/sh
date

./table_status.sh > result.txt 2>error.txt

cat error.txt | awk '{print $3," "$4," ",$19}' | grep 'Permission' | awk '{print $1," ",$2," ",$3}'  | awk -F: '{print $1," ", $2}' | sed -e 's/inode=//g' | sed -e 's/"//g' | awk '{print $3," ",$1," ",$2}' > permission.txt

rm all.txt
cat error.txt | grep "No suc" | awk -F/ '{print $7," 0"}' > nofile.txt
cat -n result.txt > all.txt
cat -n nofile.txt >> all.txt
cat -n permission.txt >> all.txt

date
