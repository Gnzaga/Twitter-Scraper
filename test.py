import sentiment
from sentiment import sentimentData

fname = input("Filename: ")

cov = sentimentData(fname)

cov.generateValues()

print("neu: " + str(cov.neu))

print("neg: " + str(cov.neg))

print("pos: " + str(cov.pos))
