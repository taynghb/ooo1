import 'dart:io';
import 'dart:math';

void main(List<String> arguments) {
  print("введите a");
  int a = int.parse(stdin.readLineSync()!);
  print("введите b");
  int b = int.parse(stdin.readLineSync()!);
  int operator;
  do {
  print("введите оператор: 1.+, 2.-, 3.*, 4./, 5.~/, 6.%, 7. степень, 8. ==, 9.!=, 10. >, 11.<, 12. >=, 13.<=, 14. И, 15.ИЛИ , 16.НЕ ");
  print("введите 0 для выхода");
  operator = int.parse(stdin.readLineSync()!);
  if (operator == 0) break;
  switch(operator){
    case 1: 
    print("$a + $b = ${a + b}");
    break;
    case 2: 
    print("$a - $b = ${a - b}");
    break;
    case 3: 
    print("$a * $b = ${a * b}");
    break;
    case 4: 
    b != 0 ? print("$a / $b = ${a / b}") : print("на 0 делить нельзя");
    break;
    case 5: 
    b != 0 ? print("$a ~/ $b = ${a ~/ b}") : print("на 0 делить нельзя");
    break;
    case 6: 
    b != 0 ? print("$a % $b = ${a % b}") : print("на 0 делить нельзя");
    break;
    case 7: 
    print("$a ^ $b = ${pow(a,b)}");
    break;
    case 8: 
    print("$a == $b = ${a == b}");
    break;
    case 9: 
    print("$a != $b = ${a != b}");
    break;
    case 10: 
    print("$a > $b = ${a > b}");
    break;
    case 11: 
    print("$a < $b = ${a < b}");
    break;
    case 12: 
    print("$a >= $b = ${a >= b}");
    break;
    case 13: 
    print("$a <= $b = ${a <= b}");
    break;
    case 14: 
    bool aBool = a != 0;
    bool bBool = b != 0;
    print("$a != 0 && $b != 0 = ${aBool && bBool}");
    break;
    case 15: 
    bool aBool = a != 0;
    bool bBool = b != 0;
    print("$a != 0 || $b != 0 = ${aBool || bBool}");
    break;
    case 16: 
    bool aBool = a != 0;
    bool bBool = b != 0;
    print("!($a != 0) = ${!aBool}");
    print("!($b != 0) = ${!bBool}");
    break;
    default: 
    print("неверная команда");
    }
  } while (operator != 0);
  }
  
  // print("введите цену товара");
  // String tovar = stdin.readLineSync()!;
  // int tovar2 = int.parse(tovar);
  // print("введите скидку");
  // String disc = stdin.readLineSync()!;
  // int disc3 = int.parse(disc);
  

  // print("введите ширину");
  // int width = int.parse(stdin.readLineSync()!);
  // print("введите высоту");
  // int height = int.parse(stdin.readLineSync()!);
  // double c = (width+height)*2;
  // print(c);

  // String s1 = "kolya";
  // String s2 = "K" + s1.substring(1);
  // // print(s2);
  // print(s2.contains("o"));
  // print(s2.split(""));
  // print(s2.split("").join());
  // print(s2.replaceFirst(s2, "a"));
  // print(s2.isEmpty);
  // print(s2.isNotEmpty);
  // String s3 = "52";
  // print(s3.padLeft(5,"0"));
// int v = 1;
// int b = 2;
// if(v>b){
//   print("v>b");
// }print("v<b");

// switch(v){
//   case 1:
//   print("1");
//   v++;
//   continue N3;
//   N3:case 2:
//   print("fghj");
//   break;
//   default:
//   print("ничего");
// }
