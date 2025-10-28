#ProcessData.py
#Name:Nola Nelson
#Date:10/28/25
#Assignment:Lab8

import random

def main():

  #Open the files we will be using
  inFile = open("names.dat", 'r')
  outFile = open("StudentList.csv", 'w')

  #Process each line of the input file and output to the CSV file
  #line = inFile.readline()
  for line in inFile:
    data = line.split()
    first = data[0]
    last = data[1]
    idNum = data[3]
    year = data[5]
    major = data [6]

    student_id = makeID(first, last, idNum)
    major_yr = majorYr(major, year)

    output = last + "," + first + "," + student_id + "," + major_yr + "\n"
    print(output)
    outFile.write(output)


  #Close files in the end to save and ensure they are not damaged.
  inFile.close()
  outFile.close()

def makeID(first, last, idNum):
  #print(first, last, idNum)
  idLen = len(idNum)

  while len(last) < 5:
    last = last + "X"

  id = first[0] + last + idNum[idLen - 3: ]
  #print(id)
  return id

def majorYr(major, year):
  majorLen = major[:3]

  if "Freshman" in year:
    yrCode = "FR"
  elif "Sophomore" in year:
    yrCode = "SO"
  elif "Junior" in year:
    yrCode = "JR"
  elif "Senior" in year:
    yrCode = "SR"
  return majorLen + "-" + yrCode


if __name__ == '__main__':
  main()
