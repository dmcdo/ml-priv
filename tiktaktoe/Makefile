default:
	javac *.java

testNoTeacher: default
	java TrainSelfMain

testTeacher: default
	java TrainTeacherMain

clean:
	rm *.class

reset:
	cp defaultweights.txt weights.txt