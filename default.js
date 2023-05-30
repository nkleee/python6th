var text = prompt("Enter your name");
if (text === null)
{text = "";}
document.write("Your name : " + text + "<br/>");

var len = text.length;
document.write("Number of characters : " + len + "<br/>");

document.write(text.charAt(2) + "<br>");
document.write(text.toUpperCase() + "<br>");
document.write(text.toLowerCase() + "<br>");

var text1 = "hi, ";
var text2 = "bye";
var text3 = text1.concat(text2);
var text4 = text1 + text2;

document.write(text3 + "<br/>");
document.write(text4 + "<br/>");

var text5 = "hello";
var result = text5.slice(0,2);
document.write(result + "<br/>");


//var lastName = "홍";
//var firstName = "길동";
//
//var fullName = lastName + firstName;
//
//console.log(fullName);
//console.log("Today is" + " a " + "beautiful day");
//console.log("My name is " + fullName);
//
//var num1 = 20;
//var num2 = 30;
//var sum = num1 + num2;
//console.log(num1 + num2);
//console.log("" + num1 + num2);
//console.log(num1 + " + " + num2 + " = " + sum);



//var name = "이승훈";
//var age = 29;
//var cgpa = 3.92;
//var lineBreak = "<br/>"
//
//document.write("이름: " + name + lineBreak);
//document.write("나이: " + age + lineBreak);
//document.write("학점: " + cgpa + lineBreak);

//console.log("123 = " + typeof 123);
//console.log("123.5 = " + typeof 123.5);
//console.log('"123" = ' + typeof "123");
//console.log("true = " + typeof true);
//console.log("false = " + typeof false);
//
//var car;
//console.log(typeof car);
//var car = "";
//console.log(typeof car);
//
//person = { firstName: "John", lastName: "Doe", age: 50, eyeColor: "blue" };
//console.log(typeof person);
//person = null;
//console.log(typeof person);
/*
document.write("Hello World2");
document.write("<h1>Welcome to JS Program</h1>");
document.write("<h2>Welcome to JS Program</h2>");
*/
//console.log("Welcome to JS Program");
//console.info("Welcome to JS Program");
//console.warn("Welcome to JS Program");
//console.error("Welcome to JS Program");
//
//alert("Welcome to JS Program");
//var a = prompt("Welcome to JS Program");
//console.log(a);