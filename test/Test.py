
'''
@author: pengjun.pj
'''

a = "spam eggs apple"
def get_list():
    return a.split()
def print_info(a):
    print a
def get_lists():
    return [print_info(x) for x in a.split()]


from functools import wraps


def makebold(fn):
    @wraps(fn)
    def wrapped():
        return "<b>" + fn() + "</b>"
    return wrapped


def makeitalic(fn):
    @wraps(fn)
    def wrapped():
        return "<i>" + fn() + "</i>"
    return wrapped


@makebold
@makeitalic
def hello():
    """a decorated hello world"""
    return "hello world"

class Test:
    def print1(self):
        print "hello"
    def print2(self):
        print "123"
        self.print1()
        
if __name__ == '__main__':
    print('result:{}   name:{}   doc:{}'.format(hello(), hello.__name__, hello.__doc__))
    t =  Test();
    t.print2();

















