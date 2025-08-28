#include <iostream>

using namespace std;

int main(){
  int n;
  cin >> n;
  int queue[10000];
  int front = 0, back = 0;
  for(int i = 0; i < n; i++){
    string command;
    cin >> command;
    if(command == "push"){
      int x;
      cin >> x;
      queue[back++] = x;
    } else if(command == "pop"){
      if(front == back) cout << -1 << '\n';
      else cout << queue[front++] << '\n';
    } else if(command == "size"){
      cout << back - front << '\n';
    } else if(command == "empty"){
      if(front == back) cout << 1 << '\n';
      else cout << 0 << '\n';
    } else if(command == "front"){
      if(front == back) cout << -1 << '\n';
      else cout << queue[front] << '\n';
    } else if(command == "back"){
      if(front == back) cout << -1 << '\n';
      else cout << queue[back - 1] << '\n';
    }
  }
  

}