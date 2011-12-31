class InnerWindow(QtGui.QWidget):
	def initUI(self):
		QtGui.QToolTip.setFont(QtGui.QFont('SansSerif', 10))
		
		#Define grid as QtGui.QGridLayout (making it easy to say hey, we're working in a grid)
		#Then set the spacing in this grid to 10 
		grid = QtGui.QGridLayout()
		grid.setSpacing(1)
		
		# Create the two labels for the fields
		teamName = QtGui.QLabel('Team Name:')
		teamScore = QtGui.QLabel('Team Score:')
		
		# Create the two fields
		teamNameEdit = QtGui.QLineEdit()
		teamScoreEdit = QtGui.QLineEdit()
		
		# Makes a button, named enterScoreButton
		enterScoreButton = QtGui.QPushButton('Enter Score', self)
		enterScoreButton.setToolTip('Enter a score')
		enterScoreButton.clicked.connect(FACT.enterScoreButtonClicked)
		
		# Defines ways to exit the application. Is later put under the
		# menubar. Also allows exiting via control-Q
		exitAction = QtGui.QAction(QtGui.QIcon('exit.png'), '&Exit', self)
		exitAction.setShortcut('Ctrl+Q')
		exitAction.setStatusTip('Exit application')
		exitAction.triggered.connect(self.close)
		
		# Add the team name label and edit field to the layout
		grid.addWidget(teamName, 1, 0)
		grid.addWidget(teamNameEdit, 1, 1)
		
		# Add the team score field
		grid.addWidget(teamScore, 2, 0)
		grid.addWidget(teamScoreEdit, 2, 1)
		
		# Add the Enter Score Button
		grid.addWidget(enterScoreButton, 3, 1)
		
		#Just for testing, display some stuff
		grid.addWidget(testName, 4, 0)
		
		# Set the layout as grid, aka QtGui.QGridLayout()
		self.setLayout(grid)