
class Parent():
    def Info1(self):
        print('Class', Parent.__name__, 'Method "Info"')

class Child1(Parent):
    pass

class Child2(Parent):
    def Info(self):
        print('Class', Child2.__name__, 'Method "Info"')

class ChildChild(Child1,Child2):
    def Info(self):
        print('Class', ChildChild.__name__, 'Method "Info"')
        
Child_1 = Child1()
Child_1.Info1()

Child_2 = Child2()
Child_2.Info()

Child_Child = ChildChild()
Child_Child.Info1()
Child_Child.Info()



