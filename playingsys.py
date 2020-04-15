import sys
#to run file in terminal --
# >py file.py argument1 argument2 argument3

# sys.stderr.write('This is stderr text\n')
# sys.stderr.flush()
# sys.stdout.write('This is stdout text\n')
# sys.stdout.flush()

print(sys.argv)

if len(sys.argv)>1:
    print(type(sys.argv[1]))
    print(float(sys.argv[1])+5)

def add(x):
    print('so you want to add {0:<4.1f}+ 5'.format(eval(x[1])))
    print('{0:<4.1f}+ 5 ={1:>4.1f}'.format(eval(x[1]),eval(x[1])+5))

add(sys.argv)