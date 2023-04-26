#include <iostream>
#include <string>
#include <cassert>


template <class T>
class Entry {

public:
    Entry* next;
    T content;

    Entry() {
        content = T(); // will work even for primitive types (ex: float, etc)
        next = nullptr;
    }

    Entry(T content) {
        this->content = content;
        this->next = nullptr;
    }

};


template <class T>
class Queue {

private:

    Entry<T>* first;
    Entry<T>* back;
    long size;


public:

    Queue() {
        first = nullptr;
        back = nullptr;
        size = 0;
    }

    bool isEmpty() { return first == nullptr; }
    
    void enqueue(T content) {
        // adds element to the back of the queue
        // O(1) operation
        Entry<T>* entry = new Entry<T>(content);
        if (this->isEmpty()) {
            first = entry;
            back = entry;
        } else {
            back->next = entry;
            back = entry;
        }
        size++;
    }

    T dequeue() {
        // removes first element from queue and returns its content
        // O(1) operation
        assert(!this->isEmpty());

        T content = first->content;
        Entry<T>* entry = first;
        first = first->next;
        delete entry; // free memory of allocated Entry
        size--;
        return content;
    }

    T peek() {
        // returns the content of the first element in the queue
        // O(1) operation
        assert(!this->isEmpty());
        
        return first->content;
    }

    void clear() {
        // removes all elements from the queue
        // O(n) operation
        while (!this->isEmpty()) {
            this->dequeue();
        }
    }

    long getSize() { return size; }

    void dump() {
        // prints the content of the queue
        // O(n) operation
        Entry<T>* entry = first;
        while (entry != nullptr) {
            std::cout << entry->content << ", ";
            entry = entry->next;
        }
        std::cout << std::endl;
    }

    ~Queue() {
        // free memory of allocated Entrys when queue is destroyed
        this->clear();
    }

	T at(long index) {
		// returns element at given index (peek at index)
        // O(n) operation
        assert(index >= 0 && index < size);

		Entry<T>* entry = first;
		for (long i = 0; i < index; i++) {
			entry = entry->next;
		}
		return entry->content;
	}

	T remove(long index) {
		// removes element at given index and returns its content (dequeue at index)
        // O(n) operation
        assert(index >= 0 && index < size);


		Entry<T>* entry = first;
		Entry<T>* previous = nullptr;
		for (long i = 0; i < index; i++) {
			previous = entry;
			entry = entry->next;
		}

		T content = entry->content;
		if (previous == nullptr) {
			first = entry->next;
		} else {
			previous->next = entry->next;
		}
		delete entry;

		size--;
		return content;
	}

	T pop() {
		// removes last element from queue and returns its content (dequeue back)
        // O(n) operation
        assert(!this->isEmpty());

		T content = back->content;
		Entry<T>* entry = back;
		if (first == back) {
			first = nullptr;
			back = nullptr;
		} else {
			Entry<T>* previous = first;
			while (previous->next != back) {
				previous = previous->next;
			}
			back = previous;
			back->next = nullptr;
		}
		delete entry;

		size--;
		return content;
	}

	void insert(long index, T content) {
		// inserts element at given index (enqueue at index)
        // O(n) operation
        assert(index >= 0 && index <= size);

		Entry<T>* entry = new Entry<T>(content);
		if (index == 0) {
			entry->next = first;
			first = entry;
		} else {
			Entry<T>* previous = first;
			for (long i = 0; i < index - 1; i++) {
				previous = previous->next;
			}
			entry->next = previous->next;
			previous->next = entry;
		}
		size++;
	}

    Queue operator+(const Queue& other) {
		// concatenates two queues (creates a new queue)
        // O(n) operation
        Queue<T> result;

        Entry<T>* entry = this->first;
        while (entry != nullptr) {
            result.enqueue(entry->content);
            entry = entry->next;
        }
        entry = other.first;
        while (entry != nullptr) {
            result.enqueue(entry->content);
            entry = entry->next;
        }
        return result;
    }
};


int main() {
    // Note: the '{}' are used to create a new scope for each test

    { // Test: int
        Queue<int> queue;

        queue.enqueue(1);
        queue.enqueue(2);
        queue.dump();

        std::cout << "deque " << queue.dequeue() << std::endl;
        queue.dump();

        queue.enqueue(3);

        std::cout << "peek " << queue.peek() << std::endl;
        queue.dump();

        std::cout << "size " << queue.getSize() << std::endl;

        queue.clear();

        std::cout << "cleared" << std::endl;
        queue.dump();

        queue.enqueue(8);
        queue.enqueue(9);
        queue.dump();

        std::cout << "deque " << queue.dequeue() << std::endl;
        queue.dump();

        std::cout << "size " << queue.getSize() << std::endl;
    }

    { // Test: strings
        std::cout << std::endl;
        Queue<std::string> queue;

        queue.enqueue("STRING 1");
        queue.enqueue("STRING 2");
        queue.dump();

        std::cout << "deque " << queue.dequeue() << std::endl;
        queue.dump();

        queue.enqueue("STRING 3");

        std::cout << "peek " << queue.peek() << std::endl;
        queue.dump();

        std::cout << "size " << queue.getSize() << std::endl;

        queue.clear();

        std::cout << "cleared" << std::endl;
        queue.dump();

        queue.enqueue("STRING 4");
        queue.enqueue("STRING 5");
        queue.dump();

        std::cout << "deque " << queue.dequeue() << std::endl;
        queue.dump();

        std::cout << "size " << queue.getSize() << std::endl;
    }

    { // Test: operator+
        std::cout << std::endl;
        Queue<int> queue1;

        queue1.enqueue(1);
        queue1.enqueue(2);
        queue1.dump();

        Queue<int> queue2;
        queue2.enqueue(3);
        queue2.enqueue(4);
        queue2.dump();

        // Creates a new queue and does not modify the original ones
        Queue<int> queue3 = queue1 + queue2;
        queue1.dump();
        queue2.dump();
        queue3.dump();

    }

	{ // Test: at, remove, insert
		std::cout << std::endl;
		Queue<int> queue;

		queue.enqueue(1);
		queue.enqueue(3);
		queue.enqueue(5);

		queue.dump();
		std::cout << "at 1: " << queue.at(1) << std::endl;

        std::cout << "removed at 1: " << queue.remove(1) << std::endl;
		queue.dump();

		queue.insert(1, 4);
		queue.dump();

		queue.insert(0, 2);
		queue.dump();

		queue.remove(1);
		queue.dump();
	}

    { // Test: assertions
        Queue<int> queue;

        // attempt to dequeue from empty queue
        queue.dequeue();
    }


    return 0;
}