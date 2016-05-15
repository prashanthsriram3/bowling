def bowling(b, f=1):
    return (sum(b) if f == 10 else
            sum(b[:3]) + bowling(b[1:], f+1) if b[0] == 10 else
            sum(b[:3]) + bowling(b[2:], f+1) if sum(b[:2]) == 10 else
            sum(b[:2]) + bowling(b[2:], f+1))


def get_score(card):
    card = card.replace('-', '0')
    b = [int(f) if f.isdigit() else 10 if f == 'X' else 10 - int(fr[i-1]) for fr in card.split() for i, f in enumerate(fr)]
    print bowling(b)

    
if __name__ == '__main__':
    get_score('54 X 8/ 62 -6 -- X X 36 X9/')
    get_score('X 7/ 72 9/ X X X 23 6/ 7/X')
    get_score('12 34 56 78 9- 12 34 56 78 9-')
    get_score('-- -- -- -- -- -- -- -- -- --')
    get_score('-/ X 45 9- 61 X X X 9/ XX6')
    get_score('X X X X X X X X X XXX')