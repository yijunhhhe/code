from votingMachine import VotingMachine

v1 = VotingMachine()
v1.voteDemocrat()
v1.voteDemocrat()
v1.voteDemocrat()
v1.voteRepublican()
for i in range(4):
    v1.voteRepublican()

print('The number of ballots cast where', v1.getTotal())

print('The winner is', v1.getWinner())