default:
	c++ binary_tree.cpp -o binary_tree.o -c
	c++ main.cpp binary_tree.o queue.o -o main.out
	./main.out
main:
	c++ queue.o binary_tree.o main.cpp -o main.out
	./main.out
all: 
	c++ queue.cpp -o queue.o -c
	c++ binary_tree.cpp -o binary_tree.o -c
	c++ queue.o binary_tree.o main.cpp -o main.out
	./main.out
