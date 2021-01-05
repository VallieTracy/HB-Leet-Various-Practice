// Create a variable called "name" that holds a string
var nam = 'Vallie';

// Create a variable called "country" that holds a string
var country = 'America';

// Create a variable called "age" that holds an integer
var age = 40;

// Create a variable called "hourlyWage" that holds an integer
var hourlyWage = 20;

// Calculate the "dailyWage" for the user
var dailyWage = hourlyWage*8;
console.log(dailyWage);
// Create a variable that holds a number as a string
var nmbr = '12';

// Create a variable called 'weeklyWage' that converts a string into an integer
var weeklyWage = parseInt(nmbr);
console.log(weeklyWage);
console.log(typeof weeklyWage);

// Create a variable called "satisfied" that holds a boolean
var satisfied = false;
console.log(typeof satisfied);

// Print out "Hello <name>!"
console.log(`Hello ${nam}!`)

// Print out what country the user entered
console.log(`Despite COVID, you traveled to ${country}. TSK TSK!`)

// Print out the user's age
console.log(`You are ${age} years old.`)

// Print out the daily wage that was calculated
console.log(`Daily wage: $${dailyWage}.`)

// Print out the weekly wage that was calculated
console.log(`I didn't actually calculate a real weekly wage...`)

// Using an IF statement to print out whether the users were satisfied
if (satisfied == true) {
    console.log(`Great, you're satisfied!!`);
}
else {
    console.log(`Bummer, you are not happy.`)
}

