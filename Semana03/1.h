

class ComplexNumber {

    public:
        double integer;
        double imaginary;
        ComplexNumber(double integerInput, double imaginaryInput){
        integer=integerInput;
        imaginary=imaginaryInput;}        ;
        ComplexNumber Sum(ComplexNumber a ,ComplexNumber b );
        ComplexNumber Sub(ComplexNumber a ,ComplexNumber b );
        ComplexNumber Mult(ComplexNumber a ,ComplexNumber  b );
        ComplexNumber Div(ComplexNumber a ,ComplexNumber b );

        void GetPolarRepresentation( ComplexNumber a );
        void GetRectangularRepresentation(ComplexNumber a );


};