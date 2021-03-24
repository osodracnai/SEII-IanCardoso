/*Ian Cardoso
11411EMT014 */

#include "1.h"
#include <iostream>
#include <complex>
    using namespace std;
    ComplexNumber ComplexNumber::Sum(ComplexNumber a , ComplexNumber b ){
        double integerResult = a.integer + b.integer;
        double imaginaryResult = a.imaginary + b.imaginary;
        return ComplexNumber(integerResult, imaginaryResult);
    }

    ComplexNumber ComplexNumber::Sub(ComplexNumber a , ComplexNumber b ){
        double integerResult = a.integer - b.integer;
        double imaginaryResult = a.imaginary - b.imaginary;
        return ComplexNumber(integerResult, imaginaryResult);
    }

    ComplexNumber ComplexNumber::Mult(ComplexNumber a , ComplexNumber b ){
        double integerResult = a.integer * b.integer;
        double imaginaryResult = a.imaginary * b.imaginary;
        return ComplexNumber(integerResult, imaginaryResult);
    }

    ComplexNumber ComplexNumber::Div(ComplexNumber a ,ComplexNumber b ){
        double integerResult = a.integer / b.integer;
        double imaginaryResult = a.imaginary / b.imaginary;
        return ComplexNumber(integerResult, imaginaryResult);
    }


    void ComplexNumber::GetPolarRepresentation(ComplexNumber a ){
        cout << std::polar (a.integer , a.imaginary)<< "\n";
    }
    void ComplexNumber::GetRectangularRepresentation(ComplexNumber a){

       cout << "x= " << a.integer << "y= "<< a.imaginary << "\n";
    }

  int main()
{
    ComplexNumber c1(1,1);
    ComplexNumber c2(2,2);

    ComplexNumber sum = c1.Sum(c1,c2);
    cout << "sum: " << sum.integer << "+" << sum.imaginary<<"i \n";

    ComplexNumber sub = c1.Sub(c1,c2);
    cout << "sub: " << sub.integer << "+" << sub.imaginary<<"i \n";

    ComplexNumber mult = c1.Mult(c1,c2);
    cout << "mult: " << mult.integer << "+" << mult.imaginary<<"i \n";

    ComplexNumber div = c1.Div(c1,c2);
    cout << "div: " << div.integer << "+" << div.imaginary<<"i \n";

    cout<< "polar form " ;
    c1.GetPolarRepresentation(c1);

    cout<< "rectangular form ";
    c1.GetRectangularRepresentation(c1);

}
