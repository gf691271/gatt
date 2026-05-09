"""LaTeX sanity checker for main.tex."""
import re

tex = open('paper/main.tex', encoding='utf-8').read()

# 1. Unresolved citations
unresolved = re.findall(r'REF\d+', tex)
print(f'Unresolved citations: {len(unresolved)}')

# 2. All \cite{...} calls
cites = re.findall(r'\\cite\{([^}]+)\}', tex)
print(f'Total \\cite calls: {len(cites)}')
keys_used = set()
for c in cites:
    for k in c.split(','):
        keys_used.add(k.strip())
print(f'Unique citation keys: {len(keys_used)}')
print(f'  Keys: {sorted(keys_used)}')

# 3. Brace balance
open_b = tex.count('{')
close_b = tex.count('}')
print(f'Brace balance: open={open_b} close={close_b} delta={open_b - close_b}')

# 4. Unicode chars
unicode_chars = set()
for ch in tex:
    if ord(ch) > 127:
        unicode_chars.add(ch)
print(f'Non-ASCII characters ({len(unicode_chars)}): {sorted(unicode_chars)}')

# 5. Sections
secs = re.findall(r'\\section\{([^}]+)\}', tex)
print(f'Sections ({len(secs)}):')
for s in secs:
    print(f'  - {s}')

# 6. Find raw $ that may break (currency vs math)
dollars = tex.count('$')
print(f'$ count (math+currency mixed; should be even or unprotected currency): {dollars}')

# 7. Check for unbalanced math mode
in_math = False
for i, ch in enumerate(tex):
    if ch == '$' and (i == 0 or tex[i-1] != '\\'):
        in_math = not in_math
print(f'Math mode balanced (final state should be False): in_math={in_math}')

# 8. Find unprotected currency (e.g., "$758 billion" — needs escape)
currency_in_text = re.findall(r'(?<!\\)\$\d', tex)
print(f'Unprotected $ before digit (likely currency needing escape): {len(currency_in_text)}')
if currency_in_text[:5]:
    print(f'  First few: {currency_in_text[:5]}')
