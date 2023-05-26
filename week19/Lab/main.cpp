#include<iostream>
#include "binary_tree.h"

using namespace std;

int main() {
    Tree tree;

    long contents [] = {13, 44, 58, 8, 1, 21, 60, 56, 87, 36, 6, 45, 90, 30, 61, 90, 18, 6, 60, 11};
    for (int i=0; i<20; i++) {
        cout << "Adding " << contents[i] << endl;
        tree.add_node(contents[i]);
        // tree.dump();
        // tree.prettyDump();
        // cout << endl;
    }

    tree.dump();
    tree.prettyDump();

    cout << "Tree does not contain 1000: " << tree.contains(1000) << endl;


    cout << "Tree contains 58: " << tree.contains(58) << endl;
    cout << "Deleting 58" << endl;
    tree.delete_node(58);

    tree.dump();
    tree.prettyDump();

    cout << "Tree contains 58: " << tree.contains(58) << endl;

    return 0;
}