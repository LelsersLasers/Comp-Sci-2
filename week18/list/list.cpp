#include <iostream>
#include <string>


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
class List {

private:

    Entry<T>* first;
    Entry<T>* back;
    long size;


public:

    List() {
        first = nullptr;
        back = nullptr;
        size = 0;
    }

    bool isEmpty() { return first == nullptr; }
    
    void enlist(T content) {
        // adds element to the back of the list
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

    T delist() {
        // removes first element from list and returns its content
        if (this->isEmpty()) { throw "List is empty"; }

        T content = first->content;
        Entry<T>* entry = first;
        first = first->next;
        delete entry;
        size--;
        return content;
    }

    T peek() {
        // returns the content of the first element in the list
        if (this->isEmpty()) { throw "List is empty"; }
        
        return first->content;
    }

    void clear() {
        // removes all elements from the list
        while (!this->isEmpty()) {
            this->delist();
        }
    }

    long getSize() { return size; }

    void dump() {
        // prints the content of the list
        Entry<T>* entry = first;
        while (entry != nullptr) {
            std::cout << entry->content << " ";
            entry = entry->next;
        }
        std::cout << std::endl;
    }

    ~List() {
        // free memory of allocated Entrys when list is destroyed
        this->clear();
    }

	T at(long index) {
		// returns element at given index (peek at index)
		if (index < 0 || index >= size) { throw "Index out of bounds"; }

		Entry<T>* entry = first;
		for (long i = 0; i < index; i++) {
			entry = entry->next;
		}
		return entry->content;
	}

	T remove(long index) {
		// removes element at given index and returns its content (delist at index)
		if (index < 0 || index >= size) { throw "Index out of bounds"; }

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
		// removes last element from list and returns its content (delist back)
		if (this->isEmpty()) { throw "List is empty"; }

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
		// inserts element at given index (enlist at index)
		if (index < 0 || index > size) { throw "Index out of bounds"; }

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

    List operator+(const List& other) {
		// concatenates two lists (creates a new list)
        List<T> result;

        Entry<T>* entry = this->first;
        while (entry != nullptr) {
            result.enlist(entry->content);
            entry = entry->next;
        }
        entry = other.first;
        while (entry != nullptr) {
            result.enlist(entry->content);
            entry = entry->next;
        }
        return result;
    }
};


int main() {
    {
        List<int> list;

        list.enlist(1);
        list.enlist(2);
        list.dump();

        std::cout << "deque " << list.delist() << std::endl;
        list.dump();

        list.enlist(3);

        std::cout << "peek " << list.peek() << std::endl;
        list.dump();

        std::cout << "size " << list.getSize() << std::endl;

        list.clear();

        std::cout << "cleared" << std::endl;
        list.dump();

        list.enlist(8);
        list.enlist(9);
        list.dump();

        std::cout << "deque " << list.delist() << std::endl;
        list.dump();

        std::cout << "size " << list.getSize() << std::endl;
    }

    {
        std::cout << std::endl;
        List<std::string> list;

        list.enlist("STRING 1");
        list.enlist("STRING 2");
        list.dump();

        std::cout << "deque " << list.delist() << std::endl;
        list.dump();

        list.enlist("STRING 3");

        std::cout << "peek " << list.peek() << std::endl;
        list.dump();

        std::cout << "size " << list.getSize() << std::endl;

        list.clear();

        std::cout << "cleared" << std::endl;
        list.dump();

        list.enlist("STRING 4");
        list.enlist("STRING 5");
        list.dump();

        std::cout << "deque " << list.delist() << std::endl;
        list.dump();

        std::cout << "size " << list.getSize() << std::endl;
    }

    {
        std::cout << std::endl;
        List<int> list;

        list.enlist(1);
        list.enlist(2);
        list.dump();

        List<int> list2;
        list2.enlist(3);
        list2.enlist(4);
        list2.dump();

        List<int> list3 = list + list2;
        list3.dump();
    }

	{
		std::cout << std::endl;
		List<int> list;

		list.enlist(1);
		list.enlist(3);
		list.enlist(5);

		list.dump();
		std::cout << "at 1: " << list.at(1) << std::endl;

		list.remove(1);
		list.dump();

		list.insert(1, 4);
		list.dump();

		list.insert(0, 2);
		list.dump();

		list.remove(1);
		list.dump();
	}


    return 0;
}