from mrjob.job import MRJob as job
from mrjob.step import MRStep as step
import os

flag = 0

class Multiply(job):

	result = open('multiplication_result.txt','w')

	def mapper1(self, _, input_line):
		global flag
		input_line = input_line.split()
		input_line = list(map(float, input_line))

		if len(input_line) == 2 and flag == 0:
			flag = 1
			return

		elif len(input_line) == 2 and flag == 1:
			row, val = input_line
			column = 0

		elif len(input_line) == 3:
			row, column, val = input_line

		file = os.environ['mapreduce_map_input_file']

		if 'M' in file:
			yield column, (0,row,val)

		elif 'v' in file:
			yield row, (1,column,val)

	def reducer1(self,keys,vals):
		matrixM = []
		matrixv = []

		for val in vals:
			if val[0] == 0:
				matrixM.append(val)

			elif val[0] == 1:
				matrixv.append(val)	

		for rM, cM, vM in matrixM:
			for rv, cv, vv in matrixv:
				yield(cM,cv), vM*vv

	def mapper2(self, key, val):
		yield key, val

	def reducer2(self,key,vals):
		sum_ = sum(vals)
		yield key, sum_
		self.result.write(str(round(key[0]))+" "+str(sum_)+"\n")

	def steps(self):return [ step(mapper = self.mapper1, reducer = self.reducer1),
		step(mapper = self.mapper2, reducer = self.reducer2) ]

if __name__ == '__main__':
	Multiply.run()