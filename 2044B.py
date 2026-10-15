import sys
def solve():
    
    t=int(input().strip())
    
    
    m={'p':'q','q':'p','w':'w'}
    for _ in range(t):
        s=input().strip()
        ans="".join(m[ch] for ch in s[::-1])
        print(ans)
if __name__ == "__main__":
    solve()
