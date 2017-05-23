#!/usr/bin/env bash
#result=${test:-UNSET}
#echo $result
#echo "---------------------"
#echo $test
#echo "---------------------"
#test="oldboy"
#echo $test
#result=${test:-UNSET}
#echo $result
#echo "---------------------"
#result1=${test1:=UNSET}
#echo $result1
#echo $test1
#echo "---------------------"
#result2=${test2:?Not Defined}
#echo $result2
#echo $test2
#echo "---------------------"
test3=1
result3=${test3:+word}
echo $result3
echo $test3