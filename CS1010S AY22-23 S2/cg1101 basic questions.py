def investment(P, R, N):
    # code that computes the amount of money earned after N years
   return round(P*(1-(R/100)**(N+1))/(1-R/100),2)


def ip_format(ip_address) -> str:
    def base_2_to_10(s:str) -> int:
        if s == '': return 0
        exponent = len(s)-1
        return int(s[0])*2**exponent + base_2_to_10(s[1:])
        
    if len(ip_address) == 8: return str(base_2_to_10(ip_address))
    return str(base_2_to_10(ip_address[:8])) + "." + ip_format(ip_address[8:])


