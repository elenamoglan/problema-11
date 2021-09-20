n = int(input('Introduceti numarul de elemente: '))
if n<10:
    l=list(map(int,input('Introduceti elementele listei: ').split(',')))
    l1=l.copy()
    print(f'a)componentele tabloului la un interval de 5 poziţii: ', end='')
    for i in l:
        print(f'{i:5}',end='')
    print('\n')
    print(f'b)numerele în ordinea inversă a introducerii în calculator: {l1[::-1]}')
    print(f'c)componentele tabloului în ordine descrescătoare: {sorted(l1, reverse=True)}')
    print('d)componentele pare: ', end='')
    d=[]
    for i in l:
        if i%2==0:
            d.append(i)
    print(d)
    print(f'e)media aritmetică a componentelor pare: {sum(d)/len(d)}')
    print(f'f)componentele impare: ', end='')
    f=[]
    for i in l:
        if i%2 != 0:
            f.append(i)
    print(f)    
    x=eval(input('Introduceti x: '))
    y=eval(input('Introduceti y: '))
    print(f'g)componentele care sunt mai mari ca x şi nu sunt divizibile cu y: ', end='')
    g=[]
    for i in l:
        if i>x and i%y != 0:
            g.append(i)
    print(g)
    print(f'h)componentele care sunt mai mari ca x şi mai mici decât y: ', end='')
    h=[]
    for i in l:
        if i>x and i<y:
            h.append(i)
    print(h)
    print(f'i)poziţiile componentelor impare negative: ', end='')
    imng=[]
    for i in range(0,len(l)):
        if l[i]%2 != 0 and l[i]<0:
            imng.append(i)
    print(imng)
    print(f'j)poziţiile componentelor ce conţin doar două cifre semnificative: ', end='')
    j=[]
    for i in range(0,len(l)):
        if l[i]>=10 and l[i]<100:
            j.append(i)
    print(j)
    print(f'k)prima componentă a tabloului inlocuita cu componenta de valoare minimă din tabloul respectiv: ', end='')
    k=l[:]
    k[0]=min(k)
    print(k)
    print(f'l)componenta de valoare minimă din tabloul respectiv inlocuita cu prima componentă a acestuia: ', end='')
    k1=l[:]
    k1[l.index(min(k))] = k1[0]
    print(k1)
    print(f'm)tablou nou, format doar din componentele pare ale tabloului introdus de la tastatură: ', d)
    print(f'n)tablou nou, format doar din componentele divizibile cu 3 ale tabloului introdus de la tastatură: ', end='')
    n=[]
    for i in l:
        if i%3==0:
            n.append(i)
    print(n)
    print(f'o)tablou nou, format doar din acele componente ale tabloului introdus de la tastatură care au cel mult patru divizori: ', end='')
    o=[]
    for k in l:
        nr_div=2
        for n in range(2,k//2+1):
            if (k % n == 0):
                nr_div+=1
        if (nr_div <= 4):
            o.append(k)
    print(o)
else:
    print(f'Numarul introdus este mai mare ca 10')
