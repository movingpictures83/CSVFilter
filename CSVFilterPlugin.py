import sys
import numpy
import random
import PyPluMA

class CSVFilterPlugin:
   def input(self, filename):
      self.myfile = filename

   def run(self):
      filestuff = open(self.myfile, 'r')
      self.firstline = filestuff.readline()
      lines = []
      for line in filestuff:
         lines.append(line)

      self.m = len(lines)
      self.samples = []
      self.bacteria = self.firstline.split(',')
      if (self.bacteria.count('\"\"') != 0):
         self.bacteria.remove('\"\"')
      self.n = len(self.bacteria)
      self.ADJ = []
      i = 0
      for i in range(self.m):
            self.ADJ.append([])
            tmpsample = []
            contents = lines[i].split(',')
            self.samples.append(contents[0])
            for j in range(self.n):
               value = int(contents[j+1].strip())
               self.ADJ[i].append(value)
            i += 1
     
      j = 0
      while (j < len(self.bacteria)):
        zeroflag = True
        for i in range(self.m):
           if (self.ADJ[i][j] != 0):
              zeroflag = False
              break
        if (zeroflag):
           self.firstline = self.firstline.replace(self.bacteria[j], "")
           if (self.firstline.find(",,") != -1):
              self.firstline = self.firstline.replace(",,", ",")
           del self.bacteria[j]
           for i in range(self.m):
              del self.ADJ[i][j]
        else:
           j += 1
      self.n = len(self.bacteria)
   def output(self, filename):
      filestuff2 = open(filename, 'w')
      
      filestuff2.write(self.firstline)

      for i in range(self.m):
         filestuff2.write(self.samples[i]+',')
         for j in range(self.n):
            filestuff2.write(str(self.ADJ[i][j]))
            if (j < self.n-1):
               filestuff2.write(",")
            else:
               filestuff2.write("\n")



