class logicalOperators:
    @staticmethod
    def ensure_logical(val):
        if not (val == True or val == False): raise Exception("oi wat type did u pass to logic operator? pls input logcal values True or False only!")
        else: return val
    @classmethod
    def logical_not(cls,x): return not cls.ensure_logical(x)
    @classmethod
    def logical_or(cls,x,y): return cls.ensure_logical(x) or cls.ensure_logical(y)
    @classmethod
    def logical_and(cls,x,y): return cls.ensure_logical(x) and cls.ensure_logical(y)

class LogicGate:
    def __init__(self,inputs:list,logical_operator):
        """make sure to give  a logical_operator that accepts the number of inputs u specify!
        no of inputs is length of list of pre-set inputs"""
        self.inputs = inputs
        self.no_of_inputs = len(self.inputs)
        self.logical_operator = logical_operator
    def connect(self, position, gate):
        if position in range(self.no_of_inputs) and self.inputs[position] is None:
            new_inputs = self.inputs[:]
            new_inputs[position] = gate
            return type(self)(new_inputs,self.logical_operator)
        return None
    def compute(self, extern_inputs):
        results = []
        for input in self.inputs:
            if input is not None:
                results.append(input.compute(extern_inputs))
            else:
                results.append(extern_inputs[0])
                del extern_inputs[0]
        # print(results)
        return self.logical_operator(*results)
class AndGate(LogicGate):
    def __init__(self,inputs = [None, None], logical_operator = logicalOperators.logical_and):
        super().__init__(inputs,logical_operator)
class OrGate(LogicGate):
    def __init__(self,inputs = [None, None], logical_operator = logicalOperators.logical_or):
        super().__init__(inputs,logical_operator)
class SingleInputLogicGate(LogicGate):
    def connect(self, gate): return super().connect(0,gate)
class NotGate(SingleInputLogicGate):
    def __init__(self,inputs = [None], logical_operator = logicalOperators.logical_not):
        super().__init__(inputs,logical_operator)
    
    
and1 = AndGate()

print(and1.compute([False, False]) is False)
print(and1.compute([False, True]) is False)
print(and1.compute([True, False]) is False)
print(and1.compute([True, True]) is True)

notg = NotGate()

print(notg.compute([False]) is True)
print(notg.compute([True]) is False)

or1 = OrGate()

print(or1.compute([False, False]))  # False
print(or1.compute([False, True]))  # True
print(or1.compute([True, False]))  # True
print(or1.compute([True, True]))  # True


or_and = AndGate().connect(0, OrGate())

print(or_and.compute([False, False, False]))  # False
print(or_and.compute([False, False, True]))  # False
print(or_and.compute([False, True, False]))  # False
print(or_and.compute([False, True, True]))  # True
print(or_and.compute([True, False, False]))  # False
print(or_and.compute([True, False, True]))  # True
print(or_and.compute([True, True, False]))  # False
print(or_and.compute([True, True, True]))  # True

or_and2 = AndGate().connect(1, OrGate())

print(or_and2.compute([False, False, False]))  # False
print(or_and2.compute([False, False, True]))  # False
print(or_and2.compute([False, True, False]))  # False
print(or_and2.compute([False, True, True]))  # False
print(or_and2.compute([True, False, False]))  # False
print(or_and2.compute([True, False, True]))  # True
print(or_and2.compute([True, True, False]))  # True
print(or_and2.compute([True, True, True]))  # True


and_not = NotGate().connect(AndGate())

or0_and_not1_and_gate = or_and.connect(1, and_not)

print(or0_and_not1_and_gate.compute([False, False, False, False]))  # False

print(or0_and_not1_and_gate.compute([True, False, False, False]))  # True
print(or0_and_not1_and_gate.compute([False, True, False, False]))  # True
print(or0_and_not1_and_gate.compute([False, False, True, False]))  # False
print(or0_and_not1_and_gate.compute([False, False, False, True]))  # False

print(or0_and_not1_and_gate.compute([True, True, False, False]))  # True
print(or0_and_not1_and_gate.compute([False, True, True, False]))  # True
print(or0_and_not1_and_gate.compute([False, False, True, True]))  # False
print(or0_and_not1_and_gate.compute([True, False, False, True]))  # True
print(or0_and_not1_and_gate.compute([True, False, True, False]))  # True
print(or0_and_not1_and_gate.compute([False, True, False, True]))  # True

print(or0_and_not1_and_gate.compute([False, True, True, True]))  # False
print(or0_and_not1_and_gate.compute([True, False, True, True]))  # False
print(or0_and_not1_and_gate.compute([True, True, False, True]))  # True
print(or0_and_not1_and_gate.compute([True, True, True, False]))  # True

print(or0_and_not1_and_gate.compute([True, True, True, True]))  # False
