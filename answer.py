def roundRobinalgo(students):
    count=len(students)
    even=1-(count&1)
    poly=students[even:]
    for _ in range(count-even):
        pairs=[(students[0],poly[0])]*even
        pairs+=[(poly[i],poly[count-i-even])for i in range(1,(count+1)//2)]
        yield(pairs)
        poly=poly[1:]+poly[:1]
def pairpeople():
    students=list(range(0,6))
    for day,pairs in enumerate(roundRobinalgo(students),1):
        sitout=set(students).difference(*pairs)
        print(day,sitout,*pairs)
pairpeople()
