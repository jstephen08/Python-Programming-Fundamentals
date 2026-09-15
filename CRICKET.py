team1=input('Enter team 1 name: ')
team2=input('Enter team 2 name: ')

toss_winner=input('Who won the toss?')
choice=input('Bat or Bowl?')

if toss_winner==team1 and choice=='bat':
    first_batting=team1
    second_batting=team2

elif toss_winner==team1 and choice=='bowl':
    first_batting=team2
    second_batting=team1

elif toss_winner==team2 and choice=='bat':
    first_batting=team2
    second_batting=team1

else:
    first_batting=team1
    second_batting=team2

print(toss_winner,'won the toss and chose to ',choice)

score1=0
score2=0

#FIRST INNINGS

print(first_batting,'batting')
for i in range(36):
    run=input('Enter runs scored(0,1,2,3,4,6 or w): ')

    if run=='w':
        print("Wicket!")

        i=i+1

    else:
        score1=score1+int(run)

print('Total score of',first_batting,'=',score1)

#SECOND INNINGS

print(second_batting,'Batting')
for i in range(36):
    run=input('Enter runs scored(0,1,2,3,4,6 0r w): ')

    if run=='w':
        print('Wicket!')

        i=i+1

    else:
        score2=score2+int(run)

print('Total score of',second_batting,'=',score2)

#RESULT
print('======MATCH RESULT======')

print(first_batting,':',score1)
print(second_batting,':',score2)

if score1>score2:
    print(first_batting,"Wins!")
elif score2>score1:
    print(second_batting,"Wins!")
else:
    print("Match Tied!")
    
