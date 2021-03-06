// Peter Cwalina & Maggie Zhao
// SoftDev1 pd7
// K#29 -- Sequential Progression
// 2018-12-19

// Find the nth Fibonacci number
var fibonacci = function(n) {
  //base case 1: the number is 0 -> return 0
	if ( n == 0 ) {
		return 0;
	}
  //base case 2: the number is 1 -> return 1
	if ( n == 1 ) {
		return 1;
	}
  //use recursion: find the n-1th and n-2th Fibonacci numbers and add them
	else {
		return fibonacci(n-1) + fibonacci(n-2);
	}
};

var displayfib = function() {
	var x = fibonacci(10);
	console.log(x);
	document.getElementById("display1").innerHTML = x;
}
// Greatest Common Divisor of a and b using Euclid's Algorithm
var gcd = function(a, b) {
  //3 variables: 2 inputs & 1 temp
  var c = a;
  var d = b;
  var x;

  //if c is a multiple of d, stop
  //otherwise, find the remainder of c and d
  while (c % d != 0) {
    x = c;
    c = d;
    d = x % d;
  }

  return d;
};

var displaygcd = function() {
	var y = gcd(120, 96);
	console.log(y);
	document.getElementById("display2").innerHTML = y;
}
//external list
var list = ["Axl Rose", "Brian May", "Chris Martin", "Dan Reynolds", "Elton John", "Freddie Mercury", "Gorillaz", "Jimi Hendrix"];

//returns a randomly selected name from a list
var randomStudent = function() {
  //Math.random() returns a pseudorandom floating point number [0,1)
  //Math.trunc() returns the integer part of a number by removing any fractional digits

  //get a random integer based on the length of the list
  var index = Math.trunc(Math.random() * list.length);

  //return the name at the randomized index
	var name = list[index];
	console.log(name);
	document.getElementById("display3").innerHTML = name;
  return name;
};

var but1 = document.getElementById("b");
var result1 = but1.addEventListener('click', displayfib);

var but2 = document.getElementById("c");
var result2 = but2.addEventListener('click', displaygcd);

var but3 = document.getElementById("d");
var result3 = but3.addEventListener('click', randomStudent);
