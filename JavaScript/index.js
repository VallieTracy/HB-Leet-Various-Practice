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
  
function scoresList(arr) {
  console.log(arr);
}

scoresList(movieScores);

console.log("Using a FOR LOOP:");
for (i = 0; i < movieScores.length; i++) {
  scoresList(movieScores[i]);
}

console.log("Using FOR EACH:");
movieScores.forEach(scoresList);