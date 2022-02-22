# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 19:21:26 2022

@author: david

CSP Projet - Nonogram
black and white
"""

import copy

class Nonogram:

    
    def __init__(self, sizeX, sizeY, gridInfo):
        self.sizeX = sizeX #columns
        self.sizeY = sizeY #rows
        self.gridInfo = gridInfo #list of 2 lists : columns info first and second row info
        self.grid = self.getEmptyGrid() #the grid with the guesses
        self.cpt = 0
        self.solved = False
                
        
        
    
    def FindMaxLength(self, lst):
        """ returns the maximum length of the largest sublist of lst
        """
        maxList = max(lst, key = lambda i: len(i))
        maxLength = len(maxList)
        
        return maxLength
        
    def __str__(self):
        """ For printing purposes
        """
        #maxLength of columns/rowns sublists
        adjustR = self.FindMaxLength(self.gridInfo[0]) #to add adjustR rows
        adjustC = self.FindMaxLength(self.gridInfo[1]) #to add adjustC cols

        currentSizeR = adjustR
                
        R = ""
        for j in range(adjustR + self.sizeY):
            R += "\n"
            currentSizeC = adjustC
            doPass = False
            for i in range(adjustC + self.sizeX):
                # top-left side of the grid
                if i<adjustC and j<adjustR:
                    R += "# "
                    
                # columns indications
                elif i>=adjustC and j<adjustR:
                    sizeC = len(self.gridInfo[0][i-adjustC])
                    if sizeC >=currentSizeR:
                        R += str(self.gridInfo[0][i-adjustC][sizeC - currentSizeR]) + " "
                    else:
                        R += "  "
                        
                # rows indications
                elif i<adjustC and j>=adjustR:
                    if len(self.gridInfo[1][j-adjustR])==currentSizeC:
                        for k in self.gridInfo[1][j-adjustR]:
                            R += str(k) + " "
                        doPass = True
                    elif not doPass:
                        R += "  "
                        
                # the playable grid
                elif i>=adjustC and j>=adjustR:
                    R += str(self.grid[j-adjustR][i-adjustC]) + " "
                    
                currentSizeC -= 1
            currentSizeR -= 1
        
        return R
    
    def getEmptyGrid(self):
        """ returns a grid 
        """
        R = []
        for j in range(self.sizeY):
            R.append([])
            for i in range(self.sizeX):
                R[j].append(" ") # initialised with 1 space
        return R
    
    def updateGrid(self, grid):
        """
        grid : list*list of int
            the grid game
        
        in order to give an updated grid
        """
        self.grid = grid

    def getColumn(self, n):
        """
        n : int
            between 0 and number of rows
        returns in a list the specific column of the grid
        """
        R = []
        for row in self.grid:
            R.append(row[n])
        return R

    def groupByOne(self, L):
        """
        count a number of unbroken ones in a row/column
        and adds it to the result list
        N.B. : the name may not be appropriate
        
        Parameters
        ----------
        L : list of int
            a row or a column.

        Returns
        -------
        a list similar to an indication
        """
        R = []
        cpt = 0
        for i in L:
            if cpt!=0 and i==0:
                R.append(cpt)
                cpt = 0
            if i==1:
                cpt +=1
        if cpt!=0:
            R.append(cpt)
        return R
    
    def checkGridSolved(self):
        """
        Checks each row and column if their groupByOne corresponds to their
        respective indications, if yes, then it's solved

        coherence checking as been directly implemented in this function
        Returns
        -------
        bool
            True if the grid solved, False otherwise
        """
        #checking columns
        for i in range(self.sizeY):
            col = self.getColumn(i)
            if (self.gridInfo[0][i]!=self.groupByOne(col)):
                return False
        
        #checking rows
        for j in range(self.sizeX):
            if (self.gridInfo[1][j]!=self.groupByOne(self.grid[j])):
                return False
        
        self.solved = True
        
        return True
    
    
    
    def naiveSolver(self, n, tmpGrid):
        """ This solver acts in some way similarly to back-track
        but the checking is done only at the end of a proposed grid
        and not while constructing the grid
        so it sometimes propose a solution without respecting indications constraints
        
        it prints when it is solved and the number of "node" checked 
        """
        # final case
        if n==self.sizeY*self.sizeX-1:
            self.cpt +=1
            
            self.updateGrid(tmpGrid)
            if self.checkGridSolved():
                print("solved!")
                print(f"'node' checked : {self.cpt}")
            else:
                self.updateGrid(self.getEmptyGrid())    
        
        
        if not self.solved:
            for k in range(2):
                
                tmpGrid[n//self.sizeX][n%self.sizeY] = k
                
                #recurse
                if n<self.sizeY*self.sizeX-1:
                    self.naiveSolver(n+1, copy.deepcopy(tmpGrid))
            
    def heurisitcSolver(self):
        """ heurisitc solver as describe in the report
        
            due to lack of time and underestimation of the difficulty of the project
            this solver will not be done on time
            although it will be updated on github
        """
        
        # A - double union
        
        # B - propagation 
        
        
        return True
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
