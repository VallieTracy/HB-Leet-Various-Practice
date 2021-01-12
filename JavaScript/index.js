// Array of movie ratings
var movieScores = [
    4.4,
    3.3,
    5.9,
    8.8,
    1.2,
    5.2,
    7.4,
    7.5,
    7.2,
    9.7,
    4.2,
    6.9
  ];
  
function testFunction(aList) {
  for (i = 0; i < aList.length; i++) {
    console.log(aList[i]);
  }
}

testFunction(movieScores);

function movieMean(aList) {
  var sum = 0;
  for (i = 0; i < aList.length; i++) {
    sum = sum + aList[i];
  }
  var movieAvg = sum / (aList.length);
  return movieAvg;
}

console.log(movieMean(movieScores));