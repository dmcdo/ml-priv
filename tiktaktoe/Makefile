GAMESFILE = games.txt

default:
	javac *.java

testNoTeacher: default
	java TrainSelfMain

testTeacher: default
	java TrainPredefinedGameMain < $(GAMESFILE)

testTeacherInteractive: default
	java TrainTeacherMain

clean:
	rm *.class

reset:
	cp defaultweights.txt weights.txt