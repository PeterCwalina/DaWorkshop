var fib = (n) =>{
  if (n<=0)
    return 0;
  else if (n<=2)
    return 1;
  else
    return fib(n-1) + fib(n-2);
};

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

var students = ['peter','amit','jared', 'a','b'];
var randomStudent = () =>{
  var choice = Math.floor(Math.random() * students.length);
  return students[choice];
};
