var fib = (n) =>{
  if (n<=0)
    return 0;
  else if (n<=2)
    return 1;
  else
    return fib(n-1) + fib(n-2);
};

var fibHelper = () =>{
  var num = fib(20);
  console.log(num);
  document.getElementById("fib").innerHTML = num;
}

var gcd = (n,d) =>{
  var x,a,b;
  a = n;
  b = d;
  while(a%b != 0){
    x = a;
    a = b;
    b = x%b;
  };
  return b;

};

var gcdHelper = () =>{
  var num = gcd(30,100);
  console.log(num);
  document.getElementById("gcd").innerHTML = num;
}

var students = ['peter','amit','jared', 'a','b'];
var randomStudent = () =>{
  var choice = Math.floor(Math.random() * students.length);
  return students[choice];
};

var ranStudentHelper = () =>{
  var student = randomStudent();
  console.log(student);
  document.getElementById("ranStudent").innerHTML = student;
}
var fibButton = document.getElementById('f');
var result1 = fibButton.addEventListener('click',fibHelper);

var gcdButton = document.getElementById('g');
var result2 = gcdButton.addEventListener('click',gcdHelper);

var studentButton = document.getElementById('r');
var result3 = studentButton.addEventListener('click',ranStudentHelper);
