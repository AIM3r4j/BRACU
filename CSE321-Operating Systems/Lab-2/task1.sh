#!/bin/bash

echo "Enter a valid BRACU ID:"
read id

if [ ${#id} -eq 8 ];
then year=${id:0:2}
if [ ${id:2:1} -eq 1 ];
then session="Spring"
elif [ ${id:2:1} -eq 2 ];
then session="Fall"
elif [ ${id:2:1} -eq 3 ];
then session="Summer"
else echo "Invalid BRACU ID" && exit 0;
fi
if [ ${id:3:2} -eq 01 ];
then echo "the student is from the Dept. of CSE enrolled in $session 20$year"
else echo "the student is not from the Dept. of CSE"
fi
else echo "Invalid BRACU ID" && exit 0;
fi