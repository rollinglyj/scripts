#!/bin/sh

date
cat ./*| awk '{a[$8]++} END {for (i in a) print i, a[i]}'|sort -n -r -k 2|head -50|cat -n
date
