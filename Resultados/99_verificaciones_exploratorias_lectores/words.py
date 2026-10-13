import sys, fitz
doc = fitz.open(sys.argv[1])
for p in [6,8]:
    pg = doc[p-1]
    ws = pg.get_text("words")
    # find 'Risk' y
    ry = [w for w in ws if w[4]=='Risk'][0][1]
    rows = {}
    for w in ws:
        if ry-2 < w[1] < ry+40 and w[3] < 300:
            rows.setdefault(round(w[1],0), []).append((round(w[0],1), w[4]))
    # also axis tick row
    print("PAGE", p)
    for y in sorted(rows):
        print(y, [t for x,t in sorted(rows[y])])
    # x positions of axis ticks
    axy = [w for w in ws if w[4]=='Months'][0][1]
    ticks = sorted([(round(w[0],1),w[4]) for w in ws if axy-20 < w[1] < axy-3 and w[4].isdigit()])
    print("ticks", ticks)
    for y in sorted(rows):
        print(y, sorted(rows[y]))
