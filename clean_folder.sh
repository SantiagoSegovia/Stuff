#!/usr/bin/bash
i=0
j=0
for var in "$@"
do
  i=$i+1
done
if [ "$i" -eq "$j" ]; then
    	path="."
else
	path=$1
fi
cd $path
rm *.log
rm *.pyc
rm *.txt
