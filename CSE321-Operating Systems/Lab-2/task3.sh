#i/bin/bash
echo "Please enter an integer: "
read number

result=$number

while [ $result != 1 ] && [ $result != 4 ]
do
        sum=0
        remainder=0
        while [ $result -gt 0 ]
        do
                remainder=$(($result % 10))
                result=$(($result / 10))
                squared=$(($remainder * $remainder))
                sum=$(($sum + $squared))
        done
        result=$sum
done

if [ $result -eq 1 ];
        then echo "It's a Happy Prime!"
elif [ $result -eq 4 ];
        then echo "It's not a Happy Prime!"
fi