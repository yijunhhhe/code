from voting_machine import VotingMachine

vm = VotingMachine()

vm.voteDemocrat()
vm.voteDemocrat()
vm.voteRepublican()
vm.voteDemocrat()
vm.voteRepublican()
vm.voteDemocrat()
vm.voteRepublican()

print("Democrats: %d    Republicans: %d" % vm.getTallies())

vm.voteDemocrat()
print("The total number of votes cast today is", vm.getTotal())

print("The winner of today's elections is ", vm.getWinner())