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


from PyQt5 import QtCore
from PyQt5 import QtGui
import model.constants
import view.constants
import logging

logger = logging.getLogger(__name__)

class recipeViewLabels(QtCore.QObject):
    def __init__(self):
        QtCore.QObject.__init__(self)
        self.typeLabels = {
            model.constants.RECIPE_TYPE_ALL_GRAIN   : self.tr('Tout grain'),
            model.constants.RECIPE_TYPE_PARTIAL_MASH    : self.tr('Extrait'),
            model.constants.RECIPE_TYPE_EXTRACT : self.tr('Partial mash'),
        }

class RecipeView(QtCore.QObject):
    def __init__(self, recipe):
        QtCore.QObject.__init__(self)
        self.model = recipe
        self.recipeViewLabels = recipeViewLabels()

    def QStandardItem_for_fermentable_proportion(self, fermentable):
        proportion = self.model.compute_proportions()[fermentable]
        item = QtGui.QStandardItem("%.0f %%" %(proportion))
        item.setData(fermentable, view.constants.MODEL_DATA_ROLE)
        return item

    def QStandardItem_for_hop_ibu(self, hop):
        ibu = self.model.compute_IBUPart()[hop]
        item = QtGui.QStandardItem("%.1f IBU" %(ibu))
        item.setData(hop, view.constants.MODEL_DATA_ROLE)
        return item

    def recipeTypeDisplay(self):
        """Return a translated string which can be used in UI for displaying recipe type"""
        try:
            return self.recipeViewLabels.typeLabels[self.model.type]
        except KeyError :
            return '?recipeTypeDisplay?'

