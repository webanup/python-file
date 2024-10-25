course={
    'php':{'duration':'2 month','fees':'12000'},
    'python':{'duration':'2 month','fees':'13000'},
    'java':{'duration':'2 month','fees':'9000'},
} 
print(course)
print(course['php']['fees'])
for k,v in course.items():
    print(k,v['duration'],v['fees'])