class Team:

	teamValue          = 0  #The true value to our team
	teamScores         = [] #List of scores 
	teamName           = '' #The team's name
	averageScore       = 0  #The average of all the team's scores
	
	def __init__(self, name):
		self.teamName = name
		
		
	def teamValueCalculation(teamScores):
		averageScore = sum(teamScores)/len(teamScores)
		for i in teamScores:
			teamValue = teamValue + (100 - abs(teamScore[i] - averageScore))
		
