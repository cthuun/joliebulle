#!/usr/bin/python3
#­*­coding: utf­8 -­*­



#joliebulle 3.5
#Copyright (C) 2010-2016 Pierre Tavares
#Copyright (C) 2012-2015 joliebulle's authors
#See AUTHORS file.

#This program is free software; you can redistribute it and/or
#modify it under the terms of the GNU General Public License
#as published by the Free Software Foundation; either version 3
#of the License, or (at your option) any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program; if not, write to the Free Software
#Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.


import PyQt5
import sys
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from preboil_ui import *



class DialogPreBoil(QtWidgets.QDialog):
    def __init__(self, parent = None):
        QtWidgets.QDialog.__init__(self,parent)
        self.ui = Ui_PreEbullitionDialog()
        self.ui.setupUi(self)

    def setData (self, preBoilVol, preBoilGravity, recipeGu, recipeVolume) :
    	self.ui.doubleSpinBoxVolume.setValue(preBoilVol)
    	self.ui.labelGravity.setText("%.3f" %(preBoilGravity))
    	self.recipeGu = recipeGu
    	self.recipeVolume = recipeVolume
    	################################
        #Connexion
        ################################
    	self.ui.doubleSpinBoxVolume.valueChanged.connect(self.theoricGravity)

    def theoricGravity (self) :
	    indice = float(self.recipeVolume)/self.ui.doubleSpinBoxVolume.value()
	    GUS = self.recipeGu * indice
	    SG = 1+(GUS/1000)
	    self.ui.labelGravity.setText("%.3f" %SG)
