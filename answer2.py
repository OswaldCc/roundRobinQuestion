def pairings_on_day(students,day):
    #create today's list by copying the original list of students
    bag=students.copy()
    pairs=[]
    #Rotate the list 
    for _ in range(day):
        bag.append(bag.pop(0))
    #remove all 2-person groups from the list
    while len(bag)>3:
        pairs.append((bag.pop(0), bag.pop(0)))
    pairs.append(tuple(bag))
    return pairs
def all_pairings(students):
    ret=[]
    for i in range(len(students)):
        ret.append(pairings_on_day(students,i))
    return ret
all_pairings([1,2,3,4,5])