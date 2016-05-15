def calc(f, bonus = 'N'):
    if f == 'X':
        return 10
    else:
        if bonus == 'Y':
            return int(f[0])
        elif f[1] == '/':
            return 10
        else:
            return int(f[0]) + int(f[1])


def get_score(card):
    card = card.replace('-', '0')
    frames = card.split()
    score = 0
    for i, f in enumerate(frames[:8]):
        score += calc(f)
        if f == 'X':
            score += calc(frames[i+1])
            if frames[i+1] == 'X':
                score += calc(frames[i+2][0], 'Y')
        elif f[1] == '/':
            score += calc(frames[i+1][0], 'Y')
            
    score += calc(frames[8])
    if frames[8] == 'X':
        if frames[9][0] == 'X':
            score += calc(frames[9][0], 'Y')
            score += calc(frames[9][1], 'Y')
        else:
            score += calc(frames[9][:2])
    elif frames[8][1] == '/':
        score += calc(frames[9][0], 'Y')
     
    if frames[9][0] == 'X':
        score += 10
        if frames[9][1] == 'X':
            score += 10
            if frames[9][2] == 'X':
                score += 10
            else:
                score += int(frames[9][2])
        else:
            score += calc(frames[9][1:]) 
    else:
        score += calc(frames[9][:2])
        if frames[9][1] == '/':
            score += calc(frames[9][2], 'Y')
                
    print score


if __name__ == '__main__':
    get_score('54 X 8/ 62 -6 -- X X 36 X9/')
    get_score('X 7/ 72 9/ X X X 23 6/ 7/X')
    get_score('12 34 56 78 9- 12 34 56 78 9-')
    get_score('-- -- -- -- -- -- -- -- -- --')
    get_score('-/ X 45 9- 61 X X X 9/ XX6')
    get_score('X X X X X X X X X XXX')