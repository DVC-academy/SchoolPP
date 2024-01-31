﻿class FirstSession
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
		//4. feladat: paraméterek és visszatérési érték
		Console.WriteLine(Sum(10, 2));


		//4.b újra írni mindent amit eddig csináltunk fgv-ként, innentől mindent függvényként csinálunk.

		Console.WriteLine("###########################");
        FirstExcercise();
		SecondExcercise();
        Console.WriteLine("###########################");



        //Még mindig nincsen értelme, mivel kézzel írjuk be a változókat előre.
        //Input bevezetése
        //5. feladat: adat bekérése a std inputról
        Console.WriteLine("Adj meg egy számot, és én hozzáadok kettőt!");
        int num = Convert.ToInt32(Console.ReadLine());
        Console.WriteLine("Az eredmény: ", num + 2);



        //Összetett feladat
        Console.WriteLine("Írd be az első számot:");
        int firstNumber = Convert.ToInt32(Console.ReadLine());
        Console.WriteLine("Írd be a második számot:");
        int secondNumber = Convert.ToInt32(Console.ReadLine());
        

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

	static void FirstExcercise()
	{
        Console.WriteLine("Első feladat:");
        Console.WriteLine("Így tudunk üzenetet kiírni.");

        string message = "Így pedig változón keresztül írhatunk ki valamit.";
        Console.WriteLine(message);

        //Konkatenáció
        string firstString = "Így lehet összekötni";
        string secondString = "két darab string-et.";

        Console.WriteLine(firstString + " " + secondString);
    }

	static void SecondExcercise()
	{
        Console.WriteLine("Második feladat:");
        Console.WriteLine(2 + 3);


        int number = 2;
        int number2 = 6;
        Console.WriteLine(number + number2);
    }


}

