const readline = require('readline');

// Arrays to store expenses and income
let expenses = [];
let income = [];

// Create readline interface
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

// Function to track expenses
function trackExpenses() {
  let totalSpent = 0;

  rl.question("Enter expense amount (or 'done' to finish): ", (expense) => {
    if (expense.toLowerCase() === "done") {
      rl.close();
      trackIncome();
      return;
    }

    expense = parseFloat(expense);
    if (isNaN(expense) || expense <= 0) {
      console.log("Invalid expense amount. Please enter a valid number.");
      trackExpenses();
      return;
    }

    expenses.push(expense);
    totalSpent += expense;
    if (totalSpent < 3000) {
      trackExpenses();
    } else {
      rl.close();
      trackIncome();
    }
  });
}

// Function to track income
function trackIncome() {
  rl.question("Enter income earned (or 'done' to finish): ", (incomeEarned) => {
    if (incomeEarned.toLowerCase() === "done") {
      rl.close();
      displayFinances();
      return;
    }

    incomeEarned = parseFloat(incomeEarned);
    if (isNaN(incomeEarned) || incomeEarned <= 0) {
      console.log("Invalid income earned. Please enter a valid number.");
      trackIncome();
      return;
    }

    income.push(incomeEarned);
    trackIncome();
  });
}

// Display the tracked expenses and income, along with total money spent and total money earned
function displayFinances() {
  console.log("Expenses:");
  expenses.forEach((expense) => {
    console.log(`Amount: $${expense.toFixed(2)}`);
  });

  console.log("\nIncome:");
  income.forEach((incomeEarned) => {
    console.log(`Amount: $${incomeEarned.toFixed(2)}`);
  });

  const totalSpent = expenses.reduce((acc, expense) => acc + expense, 0);
  const totalEarned = income.reduce((acc, incomeEarned) => acc + incomeEarned, 0);
  console.log(`\nTotal Money Spent: $${totalSpent.toFixed(2)}`);
  console.log(`Total Money Earned: $${totalEarned.toFixed(2)}`);
}

// Track expenses
trackExpenses();
