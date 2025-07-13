class LVM:
    def __init__(self):
        self.stack=[]
        self.register=None
        
    def PUSH(self,x):
        self.stack.append(x)
    
    def STORE(self):
        self.register=self.stack.pop()
    
    def LOAD(self):
        self.stack.append(self.register)
    
    def PLUS(self):
        a=self.stack.pop()
        b=self.stack.pop()
        self.stack.append(a+b)
    
    def TIMES(self):
        a=self.stack.pop()
        b=self.stack.pop()
        self.stack.append(a*b)
    
    def IFZERO(self):
        return self.stack.pop()==0
    
    def DONE(self):
        return self.stack[-1]
        
        
n=int(input())
queries=[]
st=LVM()
for i in range(n):
    query=[k for k in input().split()]
    queries.append(query)
i=0
n=len(queries)
while (i<n):
    if queries[i][0]=='DONE':
        print(st.DONE())
        break
        
    elif queries[i][0]=='PUSH':
        st.PUSH(int(queries[i][1]))
        
    elif queries[i][0]=='STORE':
        st.STORE()
        
    elif queries[i][0]=='LOAD':
        st.LOAD()
    
    elif queries[i][0]=='PLUS':
        st.PLUS()
    
    elif queries[i][0]=='TIMES':
        st.TIMES()
        
    elif queries[i][0]=='IFZERO':
        if st.IFZERO():
            i=int(queries[i][1])
            continue
    i+=1
        
    
    