#include <iostream>
#include <chrono>
#include <random>
using namespace std;

/*
void display(int array[], int n){
    for(int i = 0 ; i < n ; ++i){
        cout << array[i] << " ";
    }
    cout << endl;
}
 */

//  Codigo de ordenamiento extraido de https://www.geeksforgeeks.org/bubble-sort/
void bubblesort(int array[], size_t n){
//    int counter;
    for(int i = 0 ; i < n-1 ; ++i){
        for(int j = 0 ; j < n-i-1 ; ++j){
            if(array[j] > array[j+1]){
                swap(array[j], array[j+1]);
//                counter++;
            }
        }
    }
}

void generator_bubblesort(int size_arr){
    uniform_int_distribution<int>dis(0,100);
    random_device rd;
    cout << "Size " << size_arr << " -> ";
    int arr[size_arr];

    for(int i  = 0 ; i < size_arr ; ++i)
        arr[i] = dis(rd);

    auto start = chrono::system_clock::now();
    bubblesort(arr, size_arr);
    auto end = chrono::system_clock::now();

    chrono::duration<float,milli> duration = end-start;
    cout << duration.count() <<"ms " << endl;
    //return duration.count();
}

int partition(int array[], int low, int high){
    int pivot = array[high]; // value to compare
    int trav = low-1;

    for(int i = low ; i <= high-1 ; ++i)
        if(array[i] < pivot)
            swap(array[i], array[++trav]);

    swap(array[++trav], array[high]);
    return trav;
    // the procedure is the following:
    // trav is at low
    // we are iterating the array
    // if there is a value smaller than pivot then that value should go to the left of the array (where trav is)
    // then trav moves 1 position ahead, and we continue iterating.
    // once we finish the iteration, trav is in the center of the array with all left values smaller than pivot and all left value greater than pivot
    // the last thing to do is place pivot in the middle and return the position to call quicksort again.
}

//  Codigo de ordenamiento extraido de https://www.geeksforgeeks.org/quick-sort/
void quicksort(int array[], int low, int high){
    if(low < high){
        int part = partition(array, low, high);
        quicksort(array, low, part-1); // if part-1 is not used, it will always take the prev pivot as the new pivot.
        quicksort(array, part+1, high); //if part+1 is not used, it will probably change the position of the prev pivot (which was sorted), that may give unexpected results.
    }
}

void generator_quicksort(int size_arr){
    uniform_int_distribution<int>dis(0,100);
    random_device rd;
    cout << "Size " << size_arr << " -> ";
    int arr[size_arr];

    for(int i  = 0 ; i < size_arr ; ++i)
        arr[i] = dis(rd);

    auto start = chrono::system_clock::now();
    quicksort(arr, 0, size_arr-1);
    auto end = chrono::system_clock::now();

    chrono::duration<float,milli> duration = end-start;
    cout << duration.count() <<" ms" << endl;
    //return duration.count();
}

int main() {

    //Quicksort
    cout << "Quicksort algorithm:" << endl;
    // 10^1
    generator_quicksort(10);
    // 10^2
    generator_quicksort(100);
    // 10^3
    generator_quicksort(1000);
    // 10^4
    generator_quicksort(10000);
    // 10^5
    generator_quicksort(100000);
    // 10^6
    generator_quicksort(1000000);

    cout << endl;

    //Bubblesort
    cout << "Bubble-sort algorithm:" << endl;
    // 10^1
    generator_bubblesort(10);
    // 10^2
    generator_bubblesort(100);
    // 10^3
    generator_bubblesort(1000);
    // 10^4
    generator_bubblesort(10000);
    // 10^5
    generator_bubblesort(100000);
    // 10^6
    generator_bubblesort(1000000);

    return 0;
}
