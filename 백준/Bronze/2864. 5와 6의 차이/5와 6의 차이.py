import sys
ip = sys.stdin.readline

m,n = ip().split()

m_min = ""
m_max = ""
for i in m :
  if i == "5" or i == "6" :
    m_min += "5"
    m_max += "6"
  else :
    m_min += i
    m_max += i


n_min = ""
n_max = ""
for i in n :
  if i == "5" or i == "6" :
    n_min += "5"
    n_max += "6"
  else :
    n_min += i
    n_max += i

print(int(m_min)+int(n_min),int(m_max)+int(n_max))