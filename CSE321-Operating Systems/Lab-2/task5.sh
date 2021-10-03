#!/bin/bash
add () {
        echo "The result is "$(( $1 + $2 ))
}

sub () {
        echo "The result is "$(( $1 - $2 ))
}

mult () {
        echo "The result is "$(( $1 * $2 ))
}

div () {
        echo "The result is "$(( $1 / $2 ))
}

echo "Which operation would you like to do?"
read op

echo "Operand 1:"
read op1
echo "Operand 2:"
read op2

if [ $op == "+" ];
        then add $op1 $op2
elif [ $op == "-"  ];
        then sub $op1 $op2
elif [ $op == "*"  ];
        then mult $op1 $op2
elif [ $op == "/"  ];
        then div $op1 $op2
fi