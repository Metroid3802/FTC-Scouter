import sys
import team
import InnerWindow
from PySide import QtGui

#The main class of the FTC Alliance Calculator Tallyboard
class FACT(QtGui.QMainWindow):
	
	#Holds a list of all the teams
	teamList = []
	
	def __init__(self):
		super(FACT, self).__init__()
		
		# Set window properties such as height, name, and icon
		self.resize(770, 450)
		self.center()
		self.setWindowTitle('FTC Alliance Calculator')
		self.InnerWindow = InnerWindow(self)
		
		# Make the menu bar, add a file drop down menu, add the exit action
		menubar = self.menuBar()
		fileMenu = menubar.addMenu('&File')
		fileMenu.addAction(exitAction)
		
		# Change the fucking icon at some point, will ya?
		self.setWindowIcon(QtGui.QIcon('Wh6nc.jpg'))
		self.setCentralWidget(InnerWindow)
		self.InnerWindow.initUI
		
		
		
	#Centers the window for us
	def center(self):
		qr = self.frameGeometry()
		cp = QtGui.QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())
	
	#When the button is pressed
	def enterScoreButtonClicked(self):
		#For holding the team name until it's found or put in the list
		tempTeamName = teamNameEdit.text()
		#For holding the team score
		tempTeamScore = int(teamScoreEdit.text())
		#The position in the array that we're currently focused on
		currentTeam = 0
		#If the team doesn't exist yet, add it, and the score
		if teamList.count(tempTeamName) == 0:
			newTeam = Team(tempTeamName)
			teamList.add(newTeam)
			teamList[currentTeam].teamScores.append(tempTeamScore)
			currentTeam = currentTeam + 1
		
		#If it does, just add the score
		else:
			currentTeam = teamList.index(team)
			teamList[currentTeam].teamScores.append(tempTeamScore)
		
		
def main():
	
		app = QtGui.QApplication(sys.argv)
		fact = FACT()
		fact.show()
		sys.exit(app.exec_())

if __name__ == '__main__':
	main()
