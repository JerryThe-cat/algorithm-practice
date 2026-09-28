#include <iostream>
#include <thread>

void executeThread(){
    for(int i = 0; i < 5; i++){
        std::cout << "hello world from child thread.\n";
    }
}

int main(){
    std::thread ThreadObj(executeThread);

    for(int i = 0; i < 5; i++){
        std::cout << "hello world from main thread.\n";
    }

    ThreadObj.join();

    std::cout << "Exit main() function.\n";

    return 0;
}