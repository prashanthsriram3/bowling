def get_score(card):
    card = card.replace('-', '0')
    frames = card.split()
    score = 0
    for i, f in enumerate(frames[:8]):
        if f == 'X':
            score += 10
            if frames[i+1] == 'X':
                score += 10
                if i == 7:
                    if frames[i+2][0] == 'X':
                        score += 10
                    else:
                        score += int(frames[i+2][0])
                else:
                    if frames[i+2] == 'X':
                        score += 10
                    else:
                        score += int(frames[i+2][0])
            elif frames[i+1][1] == '/':
                score += 10
            else:
                score += int(frames[i+1][0]) + int(frames[i+1][1])
        elif f[1] == '/':
            score += 10
            if frames[i+1] == 'X':
                score += 10
            else:
                score += int(frames[i+1][0])
        else:
            score += int(f[0]) + int(f[1])
            
    if frames[8] == 'X':
        score += 10
        if frames[9][0] == 'X':
            score += 10
            if frames[9][1] == 'X':
                score += 10
            else:
                score += int(frames[9][1])
        elif frames[9][1] == '/':
            score += 10
    elif frames[8][1] == '/':
        score += 10
        if frames[9][0] == 'X':
            score += 10
        else:
            score += int(frames[9][0])
    else:
        score += int(frames[8][0]) + int(frames[8][1])
    
    if frames[9][0] == 'X':
        score += 10
        if frames[9][1] == 'X':
            score += 10
            if frames[9][2] == 'X':
                score += 10
            else:
                score += int(frames[9][2])
        elif frames[9][2] == '/':
            score += 10
        else:
            score += int(frames[9][1]) + int(frames[9][2])
    elif frames[9][1] == '/':
        score += 10 + (10 if frames[9][2] == 'X' else int(frames[9][2]))
    else:
        score += int(frames[9][0]) + int(frames[9][1])
                
    print score


if __name__ == '__main__':
    get_score('54 X 8/ 62 -6 -- X X 36 X9/')
    get_score('X 7/ 72 9/ X X X 23 6/ 7/X')
    get_score('12 34 56 78 9- 12 34 56 78 9-')
    get_score('-- -- -- -- -- -- -- -- -- --')
    get_score('-/ X 45 9- 61 X X X 9/ XX6')
    get_score('X X X X X X X X X XXX')