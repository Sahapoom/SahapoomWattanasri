class roman:
    def __init__(self, r):
        self.r = r
    # M>D>C>L>X>V>I 1000,500,100,50,10,5,1
    def __int__(self): # MMMCMXCIX = 3999 MMII = 2002
        r = self.r
        sp = [('IV',4),('IX',9),('XL',40),('XC',90),('CD',400),('CM',900)]        
        int_r = 0
        for r_sp, value in sp:
            if r_sp in r:
                i = r.find(r_sp)
                r = r[0:i]+r[i+2:]
                int_r += value
        r_val = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        for ch in r:
            if ch in r_val:
                int_r += r_val[ch]
        return int_r
        
    def __str__(self):
        return self.r
    
    def __lt__(self, rhs):
        return self.__int__() < rhs.__int__()
    
    def __add__(self, rhs):
        A = self.__int__()
        B = rhs.__int__()
        C = A+B
        rom = ''
        thou = C//1000
        hun = C%1000//100
        ten = C%100//10
        unit = C%10
        if  1 <= thou <= 4:
            rom += 'M'*thou
        else:
            return 9999999999
        if hun != 0:
            rom += ['','C','CC','CCC','CD','D','DC','DCC','DCCC','CM'][hun]
        if ten != 0:
            rom += ['','X','XX','XXX','XL','L','LX','LXX','LXXX','XC'][ten]
        if unit != 0:
            rom += ['','I','II','III','IV','V','VI','VII','VIII','IX'][unit]
        return roman(rom)
        
t, r1, r2 = input().split()
a = roman(r1); b = roman(r2)
print(a < b)
print(int(a),int(b))
print(str(a),str(b))
print(int(a + b)) 
print(str(a + b))