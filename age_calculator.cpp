#include <iostream>

using namespace std;

int main() {
    int fixedYear, fixedMonth, fixedDay;
    int birthYear, birthMonth, birthDay;

    // Input fixed date for calculation
    cout << "Enter the fixed year for calculation: ";
    cin >> fixedYear;

    cout << "Enter the fixed month for calculation (1-12): ";
    cin >> fixedMonth;

    cout << "Enter the fixed day for calculation (1-31): ";
    cin >> fixedDay;

    // Input birth details
    cout << "Enter your birth year: ";
    cin >> birthYear;

    cout << "Enter your birth month (1-12): ";
    cin >> birthMonth;

    cout << "Enter your birth day (1-31): ";
    cin >> birthDay;

    // Calculate age
    int ageYears = fixedYear - birthYear;
    int ageMonths = fixedMonth - birthMonth;
    int ageDays = fixedDay - birthDay;

    // Adjust the age if the fixed date hasn't reached the birth date this year
    if (ageMonths < 0 || (ageMonths == 0 && ageDays < 0)) {
        ageYears--;
        ageMonths = 12 + ageMonths;
    }

    // Output the calculated age
    cout << "Your age is: " << ageYears << " years, " << ageMonths << " months, and " << ageDays << " days." << endl;

    return 0;
}
