#include <iostream>

using namespace std;

int *heap;
int idx;

int LChild(int index) { return 2 * index; }

int RChild(int index) { return 2 * index + 1; }

int cmp(int a, int b) { return a - b; }

void insert(int data) {
    int curIdx = ++idx;
    while (idx != 1) {
        if (cmp(data, heap[curIdx / 2]) < 0) {
            heap[curIdx] = heap[curIdx / 2];
            curIdx = curIdx / 2;
        } else {
            break;
        }
    }
    heap[curIdx] = data;
}

int getChild(int index) {
    if (LChild(index) > idx) {
        return 0;
    } else if (LChild(index) == idx) {
        return LChild(index);
    } else {
        if (cmp(heap[LChild(index)], heap[RChild(index)]) > 0) {
            return RChild(index);
        } else {
            return LChild(index);
        }
    }

}

int pop() {
    if (idx == 0) {
        return 0;
    }

    int minData = heap[1];
    int lastData = heap[idx];

    int curIdx = 1;
    int childIdx;
    while (childIdx = getChild(curIdx)) {
        if (cmp(lastData, heap[childIdx]) < 0) {
            break;
        }
        heap[curIdx] = heap[childIdx];
        curIdx = childIdx;
    }

    heap[curIdx] = lastData;
    --idx;

    return minData;
}

int main(void) {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n;
    cin >> n;

    heap = new int[n + 1];

    for (int i = 0; i < n; i++) {
        int temp;
        cin >> temp;
        if (temp) {
            insert(temp);
        } else {
            cout << pop() << "\n";
        }
    }
}