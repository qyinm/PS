#include <iostream>
#include <queue>
#include <vector>
#define FastIO cin.tie(nullptr)->ios_base::sync_with_stdio(false)

using namespace std;

class Gear {
 public:
  vector<int> teeths;
  int mid;
  int right;
  int left;
  Gear() : teeths(8), right(2), left(6), mid(0) {}
  void rotate(int direction) {
    if (direction == -1) {
      right = (right + 1) % 8;
      left = (left + 1) % 8;
      mid = (mid + 1) % 8;
    } else {
      right = (right + 7) % 8;
      left = (left + 7) % 8;
      mid = (mid + 7) % 8;
    }
  }
};

class Gears {
 public:
  vector<Gear*> gearList;
  Gears() {
    for (int i = 0; i < 4; i++) {
      gearList.push_back(new Gear());
    }
  }
  int getScore() {
    int baseScore = 1;
    int returnScore = 0;
    for (const auto& gear : gearList) {
      if (gear->teeths[gear->mid] == 1) returnScore += baseScore;
      baseScore *= 2;
    }
    return returnScore;
  }
  pair<bool, bool> check(int index, int direction, vector<bool>& checked) {
    int leftIdx = index - 1;
    int rightIdx = index + 1;
    Gear* currGear = gearList[index];
    bool leftFlag = false, rightFlag = false;
    if (leftIdx >= 0 && !checked[leftIdx]) {
      auto* leftGear = gearList[leftIdx];
      leftFlag =
          leftGear->teeths[leftGear->right] != currGear->teeths[currGear->left];
    }
    if (rightIdx < 4 && !checked[rightIdx]) {
      auto* rightGear = gearList[rightIdx];

      rightFlag = rightGear->teeths[rightGear->left] !=
                  currGear->teeths[currGear->right];
    }

    return {leftFlag, rightFlag};
  }
  void command(int index, int direction, vector<bool>& checked) {
    if (checked[index]) return;
    checked[index] = true;
    auto [leftFlag, rightFlag] = check(index, direction, checked);

    gearList[index]->rotate(direction);
    if (leftFlag) {
      command(index - 1, -direction, checked);
    }
    if (rightFlag) {
      command(index + 1, -direction, checked);
    }
  }
};

int main() {
  FastIO;
  Gears* gears = new Gears();
  for (int i = 0; i < 4; i++) {
    for (int j = 0; j < 8; j++) {
      char c;
      cin >> c;
      gears->gearList[i]->teeths[j] = (c - '0');
    }
  }

  int k;
  cin >> k;
  vector<bool> checked(4, false);
  while (k > 0) {
    int idx, direction;
    cin >> idx >> direction;
    gears->command(idx - 1, direction, checked);
    k -= 1;
    fill(checked.begin(), checked.end(), false);
  }

  cout << gears->getScore();

  return 0;
}
