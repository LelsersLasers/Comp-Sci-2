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
        if (this->isEmpty()) { throw "Queue is empty"; }

        T content = first->content;
        Entry<T>* entry = first;
        first = first->next;
        delete entry;
        size--;
        return content;
    }

    T peek() {
        // returns the content of the first element in the queue
        if (this->isEmpty()) { throw "Queue is empty"; }
        
        return first->content;
    }

    void clear() {
        // removes all elements from the queue
        while (!this->isEmpty()) {
            this->dequeue();
        }
    }

    long getSize() { return size; }

    void dump() {
        // prints the content of the queue
        Entry<T>* entry = first;
        while (entry != nullptr) {
            std::cout << entry->content << " ";
            entry = entry->next;
        }
        std::cout << std::endl;
    }

    ~Queue() {
        this->clear();
    }

    Queue operator+(const Queue& other) {
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
    {
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

    {
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

    {
        std::cout << std::endl;
        Queue<int> queue;

        queue.enqueue(1);
        queue.enqueue(2);
        queue.dump();

        Queue<int> queue2;
        queue2.enqueue(3);
        queue2.enqueue(4);
        queue2.dump();

        Queue<int> queue3 = queue + queue2;
        queue3.dump();
    }


    return 0;
}