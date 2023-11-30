using System;

class FirstSession
{
	static void Main(string[] args)
	{
		//1. feladat: String használat
		Console.WriteLine("Így tudunk üzenetet kiírni.");

		string message = "Így pedig változón keresztül írhatunk ki valamit.";
		Console.WriteLine(message);

		//Konkatenáció
		string firstString = "Így lehet összekötni";
		string secondString = "két darab string-et.";

		Console.WriteLine(firstString + " " + secondString);


		//2. feladat: int-ek
		Console.WriteLine(2 + 3);

		
        int number = 2;
        int number2 = 6;
		Console.WriteLine(number + number2);

		//Vegyes konkatenáció

		Console.WriteLine(firstString + 2 + secondString);
        Console.WriteLine(firstString + number + secondString);

		//Átláthatóság kedvéért: String interpoláció

		string stringToBeInserted = "szöveget";
		int numberToBeInserted = 5;
		Console.WriteLine($"Beírok ide valamennyi {stringToBeInserted} és egy számot is: {numberToBeInserted}.");


        // Mi lenne ha ezt szeretnénk sokszor kiírni?
        //Újra meg újra le kéne írni ezeket. Függvények bevezetése
        //3. feladat: függvények
        FirstFunction();
		FirstFunction();
		FirstFunction();

        //Mire jók még a függvények és miért is jók a változók?
        //4. feladat: paraméterek



        //Még mindig nincsen értelme, mivel kézzel írjuk be a változókat előre.
        //Input bevezetése
        //5. feladat: adat bekérése a std inputról



        //Összetett feladat
        Console.WriteLine("Írd be az első számot:");
        int firstNumber = int.Parse(Console.ReadLine());
        Console.WriteLine("Írd be a második számot:");
        int secondNumber = int.Parse(Console.ReadLine());

		int result = Sum(firstNumber, secondNumber);
		Console.WriteLine($"Az eredmény: {result}");
    }


	static void FirstFunction()
	{
        Console.WriteLine("Ez egy üzenet a függvényen belül");

        string message = "Ez egy változóba mentett üzenet a függvényen belül";
        Console.WriteLine(message);
        Console.WriteLine(2 + 3);

        int number = 10;
        int number2 = 12;
        Console.WriteLine(number + number2);

    }

	static int Sum(int firstNumber, int secondNumber)
	{
		return firstNumber + secondNumber;
	}
}

