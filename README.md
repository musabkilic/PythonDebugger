# PythonDebugger
"Python: Write an automated Python debugger" Task for Google Code-In 2019

[![asciicast](https://asciinema.org/a/YstJjZ63IP1lL9l7YT10erWp7.svg)](https://asciinema.org/a/YstJjZ63IP1lL9l7YT10erWp7)

Bubble Sort:
```Line 2[Executed 1 times; Time spent avg:42.5μs total:42.5μs]: 'list' of type <class 'list'> changed from None to [3, 9, 4, 2, 1, 5]
Line 3[Executed 1 times; Time spent avg:47.5μs total:47.5μs]: 'iter_num' of type <class 'int'> changed from None to 5
Line 4[Executed 1 times; Time spent avg:30.0μs total:30.0μs]: 'idx' of type <class 'int'> changed from None to 0
Line 4[Executed 2 times; Time spent avg:23.75μs total:47.5μs]: 'idx' of type <class 'int'> changed from 0 to 1
Line 6[Executed 1 times; Time spent avg:20.0μs total:20.0μs]: 'temp' of type <class 'int'> changed from None to 9
Line 7[Executed 1 times; Time spent avg:20.0μs total:20.0μs]: 'list' of type <class 'list'>:
* list[1] changed from 9 to 4
Line 3[Executed 3 times; Time spent avg:30.833333333333332μs total:92.5μs]: 'list' of type <class 'list'>:
* list[2] changed from 4 to 9
Line 4[Executed 3 times; Time spent avg:23.333333333333332μs total:70.0μs]: 'idx' of type <class 'int'> changed from 1 to 2
Line 7[Executed 2 times; Time spent avg:17.5μs total:35.0μs]: 'list' of type <class 'list'>:
* list[2] changed from 9 to 2
Line 3[Executed 4 times; Time spent avg:28.125μs total:112.5μs]: 'list' of type <class 'list'>:
* list[3] changed from 2 to 9
Line 4[Executed 4 times; Time spent avg:22.5μs total:90.0μs]: 'idx' of type <class 'int'> changed from 2 to 3
Line 7[Executed 3 times; Time spent avg:17.5μs total:52.5μs]: 'list' of type <class 'list'>:
* list[3] changed from 9 to 1
Line 3[Executed 5 times; Time spent avg:26.5μs total:132.5μs]: 'list' of type <class 'list'>:
* list[4] changed from 1 to 9
Line 4[Executed 5 times; Time spent avg:22.0μs total:110.0μs]: 'idx' of type <class 'int'> changed from 3 to 4
Line 7[Executed 4 times; Time spent avg:16.875μs total:67.5μs]: 'list' of type <class 'list'>:
* list[4] changed from 9 to 5
Line 3[Executed 6 times; Time spent avg:25.416666666666668μs total:152.5μs]: 'list' of type <class 'list'>:
* list[5] changed from 5 to 9
Line 3[Executed 7 times; Time spent avg:24.285714285714285μs total:170.0μs]: 'iter_num' of type <class 'int'> changed from 5 to 4
Line 4[Executed 6 times; Time spent avg:22.916666666666668μs total:137.5μs]: 'idx' of type <class 'int'> changed from 4 to 0
Line 4[Executed 7 times; Time spent avg:21.785714285714285μs total:152.5μs]: 'idx' of type <class 'int'> changed from 0 to 1
Line 6[Executed 5 times; Time spent avg:18.5μs total:92.5μs]: 'temp' of type <class 'int'> changed from 9 to 4
Line 7[Executed 5 times; Time spent avg:17.0μs total:85.0μs]: 'list' of type <class 'list'>:
* list[1] changed from 4 to 2
Line 3[Executed 9 times; Time spent avg:22.5μs total:202.5μs]: 'list' of type <class 'list'>:
* list[2] changed from 2 to 4
Line 4[Executed 8 times; Time spent avg:21.5625μs total:172.5μs]: 'idx' of type <class 'int'> changed from 1 to 2
Line 7[Executed 6 times; Time spent avg:17.083333333333332μs total:102.5μs]: 'list' of type <class 'list'>:
* list[2] changed from 4 to 1
Line 3[Executed 10 times; Time spent avg:22.0μs total:220.0μs]: 'list' of type <class 'list'>:
* list[3] changed from 1 to 4
Line 4[Executed 9 times; Time spent avg:21.11111111111111μs total:190.0μs]: 'idx' of type <class 'int'> changed from 2 to 3
Line 3[Executed 12 times; Time spent avg:21.25μs total:255.0μs]: 'iter_num' of type <class 'int'> changed from 4 to 3
Line 4[Executed 10 times; Time spent avg:21.25μs total:212.5μs]: 'idx' of type <class 'int'> changed from 3 to 0
Line 6[Executed 7 times; Time spent avg:18.571428571428573μs total:130.0μs]: 'temp' of type <class 'int'> changed from 4 to 3
Line 7[Executed 7 times; Time spent avg:17.5μs total:122.5μs]: 'list' of type <class 'list'>:
* list[0] changed from 3 to 2
Line 3[Executed 13 times; Time spent avg:20.96153846153846μs total:272.5μs]: 'list' of type <class 'list'>:
* list[1] changed from 2 to 3
Line 4[Executed 11 times; Time spent avg:21.136363636363637μs total:232.5μs]: 'idx' of type <class 'int'> changed from 0 to 1
Line 7[Executed 8 times; Time spent avg:17.5μs total:140.0μs]: 'list' of type <class 'list'>:
* list[1] changed from 3 to 1
Line 3[Executed 14 times; Time spent avg:20.892857142857142μs total:292.5μs]: 'list' of type <class 'list'>:
* list[2] changed from 1 to 3
Line 4[Executed 12 times; Time spent avg:20.833333333333332μs total:250.0μs]: 'idx' of type <class 'int'> changed from 1 to 2
Line 3[Executed 16 times; Time spent avg:20.3125μs total:325.0μs]: 'iter_num' of type <class 'int'> changed from 3 to 2
Line 4[Executed 13 times; Time spent avg:20.76923076923077μs total:270.0μs]: 'idx' of type <class 'int'> changed from 2 to 0
Line 6[Executed 9 times; Time spent avg:18.61111111111111μs total:167.5μs]: 'temp' of type <class 'int'> changed from 3 to 2
Line 7[Executed 9 times; Time spent avg:17.5μs total:157.5μs]: 'list' of type <class 'list'>:
* list[0] changed from 2 to 1
Line 3[Executed 17 times; Time spent avg:20.441176470588236μs total:347.5μs]: 'list' of type <class 'list'>:
* list[1] changed from 1 to 2
Line 4[Executed 14 times; Time spent avg:20.357142857142858μs total:285.0μs]: 'idx' of type <class 'int'> changed from 0 to 1
Line 3[Executed 19 times; Time spent avg:20.263157894736842μs total:385.0μs]: 'iter_num' of type <class 'int'> changed from 2 to 1
Line 4[Executed 15 times; Time spent avg:20.666666666666668μs total:310.0μs]: 'idx' of type <class 'int'> changed from 1 to 0

Variable 'list' of type <class 'list'>, initiliazed at function 'bubble_sort' at line 2:
* Variable was in this list of values: ['[1, 2, 3, 4, 5, 9]', '[3, 4, 4, 2, 1, 5]', '[3, 9, 4, 2, 1, 5]', '[2, 1, 3, 4, 5, 9]', '[3, 4, 2, 1, 5, 5]', '[2, 2, 1, 4, 5, 9]', '[1, 1, 3, 4, 5, 9]', '[2, 3, 1, 4, 5, 9]', '[3, 2, 4, 1, 5, 9]', '[2, 1, 1, 4, 5, 9]', '[3, 4, 9, 2, 1, 5]', '[3, 4, 2, 9, 1, 5]', '[3, 4, 2, 1, 9, 5]', '[3, 4, 2, 2, 1, 5]', '[3, 4, 2, 1, 5, 9]', '[3, 4, 2, 1, 1, 5]', '[3, 2, 1, 1, 5, 9]', '[3, 2, 2, 1, 5, 9]', '[3, 2, 1, 4, 5, 9]']
Initial value: [3, 9, 4, 2, 1, 5]; Final value: [1, 2, 3, 4, 5, 9]
=[3, 9, 4, 2, 1, 5] after line 2; `def bubble_sort(list):`
=[3, 4, 4, 2, 1, 5] after line 7; `list[idx] = list[idx+1]`
=[3, 4, 9, 2, 1, 5] after line 3; `for iter_num in range(len(list)-1,0,-1):`
=[3, 4, 2, 2, 1, 5] after line 7; `list[idx] = list[idx+1]`
=[3, 4, 2, 9, 1, 5] after line 3; `for iter_num in range(len(list)-1,0,-1):`
=[3, 4, 2, 1, 1, 5] after line 7; `list[idx] = list[idx+1]`
=[3, 4, 2, 1, 9, 5] after line 3; `for iter_num in range(len(list)-1,0,-1):`
=[3, 4, 2, 1, 5, 5] after line 7; `list[idx] = list[idx+1]`
=[3, 4, 2, 1, 5, 9] after line 3; `for iter_num in range(len(list)-1,0,-1):`
=[3, 2, 2, 1, 5, 9] after line 7; `list[idx] = list[idx+1]`
=[3, 2, 4, 1, 5, 9] after line 3; `for iter_num in range(len(list)-1,0,-1):`
=[3, 2, 1, 1, 5, 9] after line 7; `list[idx] = list[idx+1]`
=[3, 2, 1, 4, 5, 9] after line 3; `for iter_num in range(len(list)-1,0,-1):`
=[2, 2, 1, 4, 5, 9] after line 7; `list[idx] = list[idx+1]`
=[2, 3, 1, 4, 5, 9] after line 3; `for iter_num in range(len(list)-1,0,-1):`
=[2, 1, 1, 4, 5, 9] after line 7; `list[idx] = list[idx+1]`
=[2, 1, 3, 4, 5, 9] after line 3; `for iter_num in range(len(list)-1,0,-1):`
=[1, 1, 3, 4, 5, 9] after line 7; `list[idx] = list[idx+1]`
=[1, 2, 3, 4, 5, 9] after line 3; `for iter_num in range(len(list)-1,0,-1):`

Variable 'iter_num' of type <class 'int'>, initiliazed at function 'bubble_sort' at line 3:
* Variable was in range: 1-5
Initial value: 5; Final value: 1
=5 after line 3; `for iter_num in range(len(list)-1,0,-1):`
=4 after line 3; `for iter_num in range(len(list)-1,0,-1):`
=3 after line 3; `for iter_num in range(len(list)-1,0,-1):`
=2 after line 3; `for iter_num in range(len(list)-1,0,-1):`
=1 after line 3; `for iter_num in range(len(list)-1,0,-1):`

Variable 'idx' of type <class 'int'>, initiliazed at function 'bubble_sort' at line 4:
* Variable was in range: 0-4
Initial value: 0; Final value: 0
=0 after line 4; `for idx in range(iter_num):`
=1 after line 4; `for idx in range(iter_num):`
=2 after line 4; `for idx in range(iter_num):`
=3 after line 4; `for idx in range(iter_num):`
=4 after line 4; `for idx in range(iter_num):`
=0 after line 4; `for idx in range(iter_num):`
=1 after line 4; `for idx in range(iter_num):`
=2 after line 4; `for idx in range(iter_num):`
=3 after line 4; `for idx in range(iter_num):`
=0 after line 4; `for idx in range(iter_num):`
=1 after line 4; `for idx in range(iter_num):`
=2 after line 4; `for idx in range(iter_num):`
=0 after line 4; `for idx in range(iter_num):`
=1 after line 4; `for idx in range(iter_num):`
=0 after line 4; `for idx in range(iter_num):`

Variable 'temp' of type <class 'int'>, initiliazed at function 'bubble_sort' at line 6:
* Variable was in range: 2-9
Initial value: 9; Final value: 2
=9 after line 6; `temp = list[idx]`
=4 after line 6; `temp = list[idx]`
=3 after line 6; `temp = list[idx]`
=2 after line 6; `temp = list[idx]`
Line 003: `    for iter_num in range(len(list)-1,0,-1):`; Executed 7 times; Time spent avg:20.714285714285715μs total:145.0μs
Line 004: `        for idx in range(iter_num):`; Executed 20 times; Time spent avg:20.375μs total:407.5μs
Line 005: `            if list[idx]>list[idx+1]:`; Executed 15 times; Time spent avg:20.666666666666668μs total:310.0μs
Line 006: `                temp = list[idx]`; Executed 9 times; Time spent avg:20.27777777777778μs total:182.5μs
Line 007: `                list[idx] = list[idx+1]`; Executed 9 times; Time spent avg:18.61111111111111μs total:167.5μs
Line 008: `                list[idx+1] = temp`; Executed 9 times; Time spent avg:17.5μs total:157.5μs
Total execution time: 2045.75μs
[1, 2, 3, 4, 5, 9]
Line 2[Executed 8 times; Time spent avg:33344.0625μs total:266752.5μs]: 'list' of type <class 'list'>:
* list[0] changed from 1 to 3
* list[1] changed from 2 to 9
* list[2] changed from 3 to 4
* list[3] changed from 4 to 2
* list[4] changed from 5 to 1
* list[5] changed from 9 to 5
Line 2[Executed 8 times; Time spent avg:33344.0625μs total:266752.5μs]: 'iter_num' of type <class 'NoneType'> changed from 1 to None
Line 2[Executed 8 times; Time spent avg:33344.0625μs total:266752.5μs]: 'idx' of type <class 'NoneType'> changed from 0 to None
Line 2[Executed 8 times; Time spent avg:33344.0625μs total:266752.5μs]: 'temp' of type <class 'NoneType'> changed from 2 to None
Line 3[Executed 21 times; Time spent avg:21.30952380952381μs total:447.5μs]: 'iter_num' of type <class 'int'> changed from None to 5
Line 4[Executed 16 times; Time spent avg:21.09375μs total:337.5μs]: 'idx' of type <class 'int'> changed from None to 0
Line 4[Executed 17 times; Time spent avg:20.88235294117647μs total:355.0μs]: 'idx' of type <class 'int'> changed from 0 to 1
Line 6[Executed 10 times; Time spent avg:18.5μs total:185.0μs]: 'temp' of type <class 'int'> changed from None to 9
Line 7[Executed 10 times; Time spent avg:17.5μs total:175.0μs]: 'list' of type <class 'list'>:
* list[1] changed from 9 to 4
Line 3[Executed 23 times; Time spent avg:21.52173913043478μs total:495.0μs]: 'list' of type <class 'list'>:
* list[2] changed from 4 to 9
Line 4[Executed 18 times; Time spent avg:20.694444444444443μs total:372.5μs]: 'idx' of type <class 'int'> changed from 1 to 2
Line 7[Executed 11 times; Time spent avg:17.5μs total:192.5μs]: 'list' of type <class 'list'>:
* list[2] changed from 9 to 2
Line 3[Executed 24 times; Time spent avg:21.354166666666668μs total:512.5μs]: 'list' of type <class 'list'>:
* list[3] changed from 2 to 9
Line 4[Executed 19 times; Time spent avg:20.394736842105264μs total:387.5μs]: 'idx' of type <class 'int'> changed from 2 to 3
Line 7[Executed 12 times; Time spent avg:17.5μs total:210.0μs]: 'list' of type <class 'list'>:
* list[3] changed from 9 to 1
Line 3[Executed 25 times; Time spent avg:21.2μs total:530.0μs]: 'list' of type <class 'list'>:
* list[4] changed from 1 to 9
Line 4[Executed 20 times; Time spent avg:20.25μs total:405.0μs]: 'idx' of type <class 'int'> changed from 3 to 4
Line 7[Executed 13 times; Time spent avg:17.307692307692307μs total:225.0μs]: 'list' of type <class 'list'>:
* list[4] changed from 9 to 5
Line 3[Executed 26 times; Time spent avg:21.153846153846153μs total:550.0μs]: 'list' of type <class 'list'>:
* list[5] changed from 5 to 9
Line 3[Executed 27 times; Time spent avg:20.925925925925927μs total:565.0μs]: 'iter_num' of type <class 'int'> changed from 5 to 4
Line 4[Executed 21 times; Time spent avg:20.476190476190474μs total:430.0μs]: 'idx' of type <class 'int'> changed from 4 to 0
Line 4[Executed 22 times; Time spent avg:20.227272727272727μs total:445.0μs]: 'idx' of type <class 'int'> changed from 0 to 1
Line 6[Executed 14 times; Time spent avg:17.321428571428573μs total:242.5μs]: 'temp' of type <class 'int'> changed from 9 to 4
Line 7[Executed 14 times; Time spent avg:17.5μs total:245.0μs]: 'list' of type <class 'list'>:
* list[1] changed from 4 to 2
Line 3[Executed 29 times; Time spent avg:20.603448275862068μs total:597.5μs]: 'list' of type <class 'list'>:
* list[2] changed from 2 to 4
Line 4[Executed 23 times; Time spent avg:20.108695652173914μs total:462.5μs]: 'idx' of type <class 'int'> changed from 1 to 2
Line 7[Executed 15 times; Time spent avg:17.333333333333332μs total:260.0μs]: 'list' of type <class 'list'>:
* list[2] changed from 4 to 1
Line 3[Executed 30 times; Time spent avg:20.5μs total:615.0μs]: 'list' of type <class 'list'>:
* list[3] changed from 1 to 4
Line 4[Executed 24 times; Time spent avg:20.0μs total:480.0μs]: 'idx' of type <class 'int'> changed from 2 to 3
Line 3[Executed 32 times; Time spent avg:20.390625μs total:652.5μs]: 'iter_num' of type <class 'int'> changed from 4 to 3
Line 4[Executed 25 times; Time spent avg:20.1μs total:502.5μs]: 'idx' of type <class 'int'> changed from 3 to 0
Line 6[Executed 16 times; Time spent avg:17.5μs total:280.0μs]: 'temp' of type <class 'int'> changed from 4 to 3
Line 7[Executed 16 times; Time spent avg:17.34375μs total:277.5μs]: 'list' of type <class 'list'>:
* list[0] changed from 3 to 2
Line 3[Executed 33 times; Time spent avg:20.303030303030305μs total:670.0μs]: 'list' of type <class 'list'>:
* list[1] changed from 2 to 3
Line 4[Executed 26 times; Time spent avg:20.0μs total:520.0μs]: 'idx' of type <class 'int'> changed from 0 to 1
Line 7[Executed 17 times; Time spent avg:17.205882352941178μs total:292.5μs]: 'list' of type <class 'list'>:
* list[1] changed from 3 to 1
Line 3[Executed 34 times; Time spent avg:20.220588235294116μs total:687.5μs]: 'list' of type <class 'list'>:
* list[2] changed from 1 to 3
Line 4[Executed 27 times; Time spent avg:19.90740740740741μs total:537.5μs]: 'idx' of type <class 'int'> changed from 1 to 2
Line 3[Executed 36 times; Time spent avg:20.0μs total:720.0μs]: 'iter_num' of type <class 'int'> changed from 3 to 2
Line 4[Executed 28 times; Time spent avg:19.910714285714285μs total:557.5μs]: 'idx' of type <class 'int'> changed from 2 to 0
Line 6[Executed 18 times; Time spent avg:17.5μs total:315.0μs]: 'temp' of type <class 'int'> changed from 3 to 2
Line 7[Executed 18 times; Time spent avg:17.22222222222222μs total:310.0μs]: 'list' of type <class 'list'>:
* list[0] changed from 2 to 1
Line 3[Executed 37 times; Time spent avg:19.93243243243243μs total:737.5μs]: 'list' of type <class 'list'>:
* list[1] changed from 1 to 2
Line 4[Executed 29 times; Time spent avg:19.74137931034483μs total:572.5μs]: 'idx' of type <class 'int'> changed from 0 to 1
Line 3[Executed 39 times; Time spent avg:19.743589743589745μs total:770.0μs]: 'iter_num' of type <class 'int'> changed from 2 to 1
Line 4[Executed 30 times; Time spent avg:19.833333333333332μs total:595.0μs]: 'idx' of type <class 'int'> changed from 1 to 0

Variable 'list' of type <class 'list'>, initiliazed at function 'bubble_sort' at line 2:
* Variable was in this list of values: ['[1, 2, 3, 4, 5, 9]', '[3, 4, 4, 2, 1, 5]', '[3, 9, 4, 2, 1, 5]', '[2, 1, 3, 4, 5, 9]', '[3, 4, 2, 1, 5, 5]', '[2, 2, 1, 4, 5, 9]', '[1, 1, 3, 4, 5, 9]', '[2, 3, 1, 4, 5, 9]', '[3, 2, 4, 1, 5, 9]', '[2, 1, 1, 4, 5, 9]', '[3, 4, 9, 2, 1, 5]', '[3, 4, 2, 9, 1, 5]', '[3, 4, 2, 1, 9, 5]', '[3, 4, 2, 2, 1, 5]', '[3, 4, 2, 1, 5, 9]', '[3, 4, 2, 1, 1, 5]', '[3, 2, 1, 1, 5, 9]', '[3, 2, 2, 1, 5, 9]', '[3, 2, 1, 4, 5, 9]']
Initial value: [3, 9, 4, 2, 1, 5]; Final value: [1, 2, 3, 4, 5, 9]
=[3, 9, 4, 2, 1, 5] after line 2; `def bubble_sort(list):`
=[3, 4, 4, 2, 1, 5] after line 7; `list[idx] = list[idx+1]`
=[3, 4, 9, 2, 1, 5] after line 3; `for iter_num in range(len(list)-1,0,-1):`
=[3, 4, 2, 2, 1, 5] after line 7; `list[idx] = list[idx+1]`
=[3, 4, 2, 9, 1, 5] after line 3; `for iter_num in range(len(list)-1,0,-1):`
=[3, 4, 2, 1, 1, 5] after line 7; `list[idx] = list[idx+1]`
=[3, 4, 2, 1, 9, 5] after line 3; `for iter_num in range(len(list)-1,0,-1):`
=[3, 4, 2, 1, 5, 5] after line 7; `list[idx] = list[idx+1]`
=[3, 4, 2, 1, 5, 9] after line 3; `for iter_num in range(len(list)-1,0,-1):`
=[3, 2, 2, 1, 5, 9] after line 7; `list[idx] = list[idx+1]`
=[3, 2, 4, 1, 5, 9] after line 3; `for iter_num in range(len(list)-1,0,-1):`
=[3, 2, 1, 1, 5, 9] after line 7; `list[idx] = list[idx+1]`
=[3, 2, 1, 4, 5, 9] after line 3; `for iter_num in range(len(list)-1,0,-1):`
=[2, 2, 1, 4, 5, 9] after line 7; `list[idx] = list[idx+1]`
=[2, 3, 1, 4, 5, 9] after line 3; `for iter_num in range(len(list)-1,0,-1):`
=[2, 1, 1, 4, 5, 9] after line 7; `list[idx] = list[idx+1]`
=[2, 1, 3, 4, 5, 9] after line 3; `for iter_num in range(len(list)-1,0,-1):`
=[1, 1, 3, 4, 5, 9] after line 7; `list[idx] = list[idx+1]`
=[1, 2, 3, 4, 5, 9] after line 3; `for iter_num in range(len(list)-1,0,-1):`
=[3, 9, 4, 2, 1, 5] after line 2; `def bubble_sort(list):`
=[3, 4, 4, 2, 1, 5] after line 7; `list[idx] = list[idx+1]`
=[3, 4, 9, 2, 1, 5] after line 3; `for iter_num in range(len(list)-1,0,-1):`
=[3, 4, 2, 2, 1, 5] after line 7; `list[idx] = list[idx+1]`
=[3, 4, 2, 9, 1, 5] after line 3; `for iter_num in range(len(list)-1,0,-1):`
=[3, 4, 2, 1, 1, 5] after line 7; `list[idx] = list[idx+1]`
=[3, 4, 2, 1, 9, 5] after line 3; `for iter_num in range(len(list)-1,0,-1):`
=[3, 4, 2, 1, 5, 5] after line 7; `list[idx] = list[idx+1]`
=[3, 4, 2, 1, 5, 9] after line 3; `for iter_num in range(len(list)-1,0,-1):`
=[3, 2, 2, 1, 5, 9] after line 7; `list[idx] = list[idx+1]`
=[3, 2, 4, 1, 5, 9] after line 3; `for iter_num in range(len(list)-1,0,-1):`
=[3, 2, 1, 1, 5, 9] after line 7; `list[idx] = list[idx+1]`
=[3, 2, 1, 4, 5, 9] after line 3; `for iter_num in range(len(list)-1,0,-1):`
=[2, 2, 1, 4, 5, 9] after line 7; `list[idx] = list[idx+1]`
=[2, 3, 1, 4, 5, 9] after line 3; `for iter_num in range(len(list)-1,0,-1):`
=[2, 1, 1, 4, 5, 9] after line 7; `list[idx] = list[idx+1]`
=[2, 1, 3, 4, 5, 9] after line 3; `for iter_num in range(len(list)-1,0,-1):`
=[1, 1, 3, 4, 5, 9] after line 7; `list[idx] = list[idx+1]`
=[1, 2, 3, 4, 5, 9] after line 3; `for iter_num in range(len(list)-1,0,-1):`

Variable 'iter_num' of type <class 'int'>, initiliazed at function 'bubble_sort' at line 3:
* Variable was in range: 1-5
Initial value: 5; Final value: 1
=5 after line 3; `for iter_num in range(len(list)-1,0,-1):`
=4 after line 3; `for iter_num in range(len(list)-1,0,-1):`
=3 after line 3; `for iter_num in range(len(list)-1,0,-1):`
=2 after line 3; `for iter_num in range(len(list)-1,0,-1):`
=1 after line 3; `for iter_num in range(len(list)-1,0,-1):`
=None after line 2; `def bubble_sort(list):`
=5 after line 3; `for iter_num in range(len(list)-1,0,-1):`
=4 after line 3; `for iter_num in range(len(list)-1,0,-1):`
=3 after line 3; `for iter_num in range(len(list)-1,0,-1):`
=2 after line 3; `for iter_num in range(len(list)-1,0,-1):`
=1 after line 3; `for iter_num in range(len(list)-1,0,-1):`

Variable 'idx' of type <class 'int'>, initiliazed at function 'bubble_sort' at line 4:
* Variable was in range: 0-4
Initial value: 0; Final value: 0
=0 after line 4; `for idx in range(iter_num):`
=1 after line 4; `for idx in range(iter_num):`
=2 after line 4; `for idx in range(iter_num):`
=3 after line 4; `for idx in range(iter_num):`
=4 after line 4; `for idx in range(iter_num):`
=0 after line 4; `for idx in range(iter_num):`
=1 after line 4; `for idx in range(iter_num):`
=2 after line 4; `for idx in range(iter_num):`
=3 after line 4; `for idx in range(iter_num):`
=0 after line 4; `for idx in range(iter_num):`
=1 after line 4; `for idx in range(iter_num):`
=2 after line 4; `for idx in range(iter_num):`
=0 after line 4; `for idx in range(iter_num):`
=1 after line 4; `for idx in range(iter_num):`
=0 after line 4; `for idx in range(iter_num):`
=None after line 2; `def bubble_sort(list):`
=0 after line 4; `for idx in range(iter_num):`
=1 after line 4; `for idx in range(iter_num):`
=2 after line 4; `for idx in range(iter_num):`
=3 after line 4; `for idx in range(iter_num):`
=4 after line 4; `for idx in range(iter_num):`
=0 after line 4; `for idx in range(iter_num):`
=1 after line 4; `for idx in range(iter_num):`
=2 after line 4; `for idx in range(iter_num):`
=3 after line 4; `for idx in range(iter_num):`
=0 after line 4; `for idx in range(iter_num):`
=1 after line 4; `for idx in range(iter_num):`
=2 after line 4; `for idx in range(iter_num):`
=0 after line 4; `for idx in range(iter_num):`
=1 after line 4; `for idx in range(iter_num):`
=0 after line 4; `for idx in range(iter_num):`

Variable 'temp' of type <class 'int'>, initiliazed at function 'bubble_sort' at line 6:
* Variable was in range: 2-9
Initial value: 9; Final value: 2
=9 after line 6; `temp = list[idx]`
=4 after line 6; `temp = list[idx]`
=3 after line 6; `temp = list[idx]`
=2 after line 6; `temp = list[idx]`
=None after line 2; `def bubble_sort(list):`
=9 after line 6; `temp = list[idx]`
=4 after line 6; `temp = list[idx]`
=3 after line 6; `temp = list[idx]`
=2 after line 6; `temp = list[idx]`
Line 003: `    for iter_num in range(len(list)-1,0,-1):`; Executed 14 times; Time spent avg:19061.25μs total:266857.5μs
Line 004: `        for idx in range(iter_num):`; Executed 40 times; Time spent avg:19.625μs total:785.0μs
Line 005: `            if list[idx]>list[idx+1]:`; Executed 30 times; Time spent avg:19.833333333333332μs total:595.0μs
Line 006: `                temp = list[idx]`; Executed 18 times; Time spent avg:20.0μs total:360.0μs
Line 007: `                list[idx] = list[idx+1]`; Executed 18 times; Time spent avg:17.5μs total:315.0μs
Line 008: `                list[idx+1] = temp`; Executed 18 times; Time spent avg:17.22222222222222μs total:310.0μs
Total execution time: 30655.0μs```
