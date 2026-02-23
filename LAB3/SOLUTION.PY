def solve():
    n = int(input("Enter the number of items: "))
    tokens = input("E").strip().split()
    
    total = 0
    multi = 0
    mx = 0
    
    for i in range(n):
        p = int(tokens[i])
        t = (p + 9) // 10
        total += t
        if t > 1 :
            multi += 1
        if t > mx:
            mx = t
            
    print(total,multi,mx)
    

if __name__ == "__main__":
    solve()
    
    