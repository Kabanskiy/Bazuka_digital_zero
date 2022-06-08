class Name:
    a = 1 # public
    _b = 2 # protected
    __c = 3 # private

ex = Name()
print(ex.a)
print(ex._b)
print(ex._Name__c) # специальный синтаксис для приватного