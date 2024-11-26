#include <iostream>
#include <map>
using namespace std;

class Node {
    public:
        char data;
        Node* leftNode = nullptr;
        Node* rightNode = nullptr;

        Node(char data) : data(data) {}
};

bool isContain(const map<char, Node*>& map, char key) {
    return map.find(key) != map.end();
}

void preorder(const Node* node) {
    if (node == nullptr) {
        return;
    }
    cout << node->data;
    preorder(node->leftNode);
    preorder(node->rightNode);  
}

void inorder(const Node* node) {
    if (node == nullptr) {
        return;
    }
    inorder(node->leftNode);
    cout << node->data;
    inorder(node->rightNode);
}

void postorder(const Node* node) {
    if (node == nullptr) {
        return;
    }
    postorder(node->leftNode);
    postorder(node->rightNode);
    cout << node->data;
}

int main() {
    int n;
    cin >> n;

    map<char, Node*> nodeMap;

    for (int i = 0; i < n; i++) {
        char data, left, right;
        cin >> data >> left >> right;
        
        Node* node;
        if (!isContain(nodeMap, data)) {
            node = new Node(data);
            nodeMap[data] = node;
        } else {
            node = nodeMap[data];
        }

        if (left != '.') {
            Node* leftNode = new Node(left);
            node->leftNode = leftNode;
            nodeMap[left] = leftNode;
        }

        if (right != '.') {
            Node* rightNode = new Node(right);
            node->rightNode = rightNode;
            nodeMap[right] = rightNode;
        }
    }

    const auto& root = nodeMap['A'];
    preorder(root);
    cout << "\n";
    inorder(root);
    cout << "\n";
    postorder(root);

    return 0;
}