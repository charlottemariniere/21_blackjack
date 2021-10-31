import random, os, sys
from breezypythongui import EasyFrame


class BlackjackDemo(EasyFrame):

    def __init__(self):
        """GUI"""

        EasyFrame.__init__(self, title="21 BlackJack")

        # You

        self.addLabel(text="YOU", row=1, column=3)
        self.youScoreField = self.addFloatField(value=5, row=2, column=3)
        self.youHandField = self.addTextField(text="Computer current hand", row=3, column=3)
        self.youTotalField = self.addFloatField(value=0, row=4, column=3)

        # Computer
        self.addLabel(text="COMPUTER", row=1, column=5)
        self.computerScoreField = self.addFloatField(value=7, row=2, column=5)
        self.computerHandField = self.addTextField(text="Your current hand", row=3, column=5)
        self.computerTotalField = self.addFloatField(value=0, row=4, column=5)

        # Labels

        self.addLabel(text="Score", row=2, column=1)
        self.addLabel(text="Hand", row=3, column=1,)
        self.addLabel(text="Total", row=4, column=1)
        self.addLabel(text="", row=5, column=3)

        # The command buttons

        self.addButton(text="Hit", row=6, column=1) # command=self.computeTax
        self.addButton(text="Stand", row=6, column=3)
        self.addButton(text="Quit", row=6, column=5)

        # Results
        self.addTextField(text="", row=7, column=3)








BlackjackDemo().mainloop()
