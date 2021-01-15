var my_string = "I yam what I yam therefore I yam";

function word_counting(a_str) {
  str_arr = a_str.split(" ");
  word_obj = {};

  for (i = 0; i < str_arr.length; i++) {
    var currentWord = str_arr[i];
    if (currentWord in word_obj) {
      word_obj[currentWord] += 1;
    }
    else {
      word_obj[currentWord] = 1;
    }
  }

  return word_obj;

}

console.log(word_counting(my_string));

var people = {
  mom: "wilma flintstone",
  dad: "fred flintstone",
  daughter: "pebbles",
  son: "bambam"
};

console.log(Object.entries(people));

