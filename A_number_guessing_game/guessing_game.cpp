#include <iostream>
#include <string>
#include <ctime>

using namespace std;


void ask(int& inp){
    cout << "Guess a number >>> ";
    cin >> inp;

    if (cin.fail()) {
        cout << "Error" << endl;
        cin.clear();
        cin.ignore(256,'\n');
        ask(inp);
    }
}

int main(){
    int times = 0;
    int Input = 0;
    bool won = false;

    srand(time(NULL));
    int guessNumber = rand() % 100 + 1; // 1 to 100

    cout << "lets play a game\n";
    cout << "I have a secret number. Lets see if you can guess it.\n\n";

    while (times < 10 && !won){
        ask(Input);
        if (Input == guessNumber){
            won = true;
            cout << "You won. The number is " + to_string(guessNumber) + "\n";
        } 
        else if (Input < guessNumber){
            cout << "The number is Bigger than the input\n";
        }
        else if (Input > guessNumber){
            cout << "The number is Smaller than the input\n";
        }
        times += 1;
    }

    if (!won)
        cout << "Sorry, you lost. Better luck next time.\n";

    system("pause");
    return 0;
}