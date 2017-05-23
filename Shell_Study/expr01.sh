#!/usr/bin/env bash
expr 2 + 2
expr 2 - 2
expr 2 \* 2
expr 2 / 2
echo "---------------------"
i=5
i=`expr $i + 6`#变量和数字符号两边都要有空格
echo $i
echo "---------------------"
