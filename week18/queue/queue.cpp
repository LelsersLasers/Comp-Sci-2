#include <iostream>


using T = float;


class Entry {

public:
    Entry* next;
    T content;

    Entry() {
        content = 0;
        next = nullptr;
    }

    Entry(T content) {
        this->content = content;
        this->next = nullptr;
    }

};


class Queue {

private:

    Entry* first;
    Entry* back;
    long size;

    bool isEmpty() { return size == 0; }

public:

    Queue() {
        first = nullptr;
        back = nullptr;
        size = 0;
    }
    
    void enqueue(T content) {
        // adds element to the back of the queue
        Entry* entry = new Entry(content);
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
        Entry* entry = first;
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
        Entry* entry = first;
        while (entry != nullptr) {
            std::cout << entry->content << " ";
            entry = entry->next;
        }
        std::cout << std::endl;
    }
};


int main() {
    Queue queue;

    queue.enqueue(1);
    queue.enqueue(2);
    queue.dump();

    std::cout << queue.dequeue() << std::endl;
    queue.dump();

    queue.enqueue(3);

    std::cout << queue.peek() << std::endl;
    queue.dump();

    std::cout << queue.getSize() << std::endl;

    queue.clear();
    queue.dump();


    return 0;
}

