#include <iostream>
#include <string>

// assert(condition) - if condition is false, the program will stop
#include <cassert>


template <class T>
class Entry {
// Entry in a singly linked list queue

public:
    Entry* next; // pointer to next element in the queue
    T content; // content of the entry

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
// Singly linked list queue

private:

    Entry<T>* first; // first element in the queue
    Entry<T>* back; // last element in the queue
    long size; // number of elements in the queue (size of the queue)


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