for(var i = 1; i <= 100; i++) {
    if(i == 20) {
        break;
    }
    document.write(i + "<br/>");
}
document.write("===========<br/>");
for(var j = 1; j <= 100; j++) {
    if(j == 20) {
        continue;
    }
    document.write(j + "<br/>");
}
j
//var i = 1;
//
//do {
//    document.write("멋쟁이사자i : " + i++ + "<br/>");
//} while (i < 1)
//
//document.write("==============================<br/>")
//var j = 1;
//while(j < 1) {
//    document.write("멋쟁이사자j : " + j++ + "<br/>");
//}

//var digit = parseInt(prompt("숫자 입력 : "));
//
//switch (digit) {
//    case 0:
//        document.write("Zero");
//        break;
//    case 1:
//        document.write("One");
//        break;
//    case 2:
//        document.write("Two");
//        break;
//    case 3:
//        document.write("Three");
//        break;
//    case 4:
//        document.write("Four");
//        break;
//    case 5:
//        document.write("Five");
//        break;
//    case 6:
//        document.write("Six");
//        break;
//    case 7:
//        document.write("Seven");
//        break;
//    case 8:
//        document.write("Eight");
//        break;
//    case 9:
//        document.write("Nine");
//        break;
//    default:
//        document.write("Not a digit")
//}

//var letter = prompt("Enter a letter : ");
//
//letter = letter.toLowerCase();
//
//if(letter == "a" || letter == "e" || letter == "i" || letter == "o" || letter == "u" ) {
//    console.log("Vowel");
//} else {
//    console.log("Consonant");
//}

//var num1 = parseFloat(prompt("첫번째 숫자 입력 : "));
//var num2 = parseFloat(prompt("두번째 숫자 입력 : "));
//
//if(num1 > num2) {
//    console.log("큰 수는 num1 : " + num1);
//}
//
//if(num1 < num2) {
//    console.log("큰 수는 num2 : " + num2);
//}
//
//if(num1 == num2) {
//    console.log("값이 동일합니다");
//}
//
//if(num1 > num2){
//    console.log("큰 수 num1: " + num1);
//} else if (num1 < num2) {
//    console.log("큰 수 num2: " + num2);
//} else if (num1 == num2) {
//    console.log("값이 동일합니다");
//}
//
//if(num1 > num2){
//    console.log("큰 수 num1: " + num1);
//} else if (num1 < num2) {
//    console.log("큰 수 num2: " + num2);
//} else (num1 == num2) {
//    console.log("값이 동일합니다");
//}

//var num1 = 20;
//var num2 = 10;
//var num3 = "10";
//var num4 = 20;
//var num5 = 15;
//console.log("일반 크기비교");
//console.log(num1 > num2, num1, ">", num2);
//console.log(num1 >= num2, num1, ">=", num2);
//console.log(num1 < num2, num1, "<", num2);
//console.log(num1 <= num2, num1, "<=", num2);
//console.log("같은지 여부확인");
//console.log(num1 == num4, num1, "==", num2);
//console.log(num1 != num4, num1, "!=", num2);
//console.log("===");
//console.log(num1 === num3, num1, "===", num2);
//console.log(num2 === num3, num1, "===", num2);
//console.log(num2 == num3, num1, "==", num2);
//
//console.log("num1 > num2 && num1 > num5: " , num1 > num2 && !(num1 < num5));
//console.log("num1 > num2 || num1 > num5: " , num1 > num2 || num1 < num5);


//var cels = parseFloat(prompt("썹씨 입력: "));
//var farn = cels * (9 / 5) + 32;
//
//document.write("화씨: " + farn);


//var base = parseFloat(prompt("밑변 입력 : "));
//var height = parseFloat(prompt("높이 입력 : "));
//
//var area = base * height * 0.5;
//
//document.write("삼각형의 넓이 : " + area);

//var input1 = parseInt(prompt("Enter first number : "));
//var num1 = parseInt(input1);
//
//var num2 = parseInt(prompt("Enter second number : "));
//var lineBreak = "<br/>";
//
//var result = num1 + num2;
//document.write("the sum is : " + result + lineBreak);
//result = num1 - num2;
//document.write("the sub is : " + result + lineBreak);
//result = num1 * num2;
//document.write("the multi is : " + result + lineBreak);
//result = num1 / num2;
//document.write("the division is : " + result + lineBreak);
//result = num1 % num2;
//document.write("the remainder is : " + result + lineBreak);

//var num = "20";
//num = num.toString();
//console.log(typeof num);
//
//var number = 20;
//console.log(typeof number);
//
//number = number.toString();
//console.log(number, typeof number);
//
//var x = 2.56789;
//console.log(x.toFixed(1), typeof x.toFixed(1));
//console.log(x.toFixed(2));
//
//console.log(x.toPrecision(1), typeof x.toPrecision(1));
//console.log(x.toPrecision(2));
//
//console.log(Number(true));
//console.log(Number(false));
//console.log(Number(" 10"));
//console.log(Number(" 10 "));
//console.log(Number("10.25"));

//var text = prompt("Enter your name");
//if (text === null)
//{text = "";}
//document.write("Your name : " + text + "<br/>");
//
//var len = text.length;
//document.write("Number of characters : " + len + "<br/>");
//
//document.write(text.charAt(2) + "<br>");
//document.write(text.toUpperCase() + "<br>");
//document.write(text.toLowerCase() + "<br>");
//
//var text1 = "hi, ";
//var text2 = "bye";
//var text3 = text1.concat(text2);
//var text4 = text1 + text2;
//
//document.write(text3 + "<br/>");
//document.write(text4 + "<br/>");
//
//var text5 = "hello";
//var result = text5.slice(0,2);
//document.write(result + "<br/>");


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