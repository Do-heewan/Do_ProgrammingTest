m_w, m_b = map(int, input().split())
t_w, t_b = map(int, input().split())
p_w, p_b = map(int, input().split())

a = min(m_w, t_b, p_w)
b = min(m_b, t_w, p_b)

print(min(a + b, 2 * min(a, b) + 1))