



// Arrays to store expenses and income
let expenses = [];
let income = [];

// Function to track expenses
function trackExpenses() {
  let totalSpent = 0;

  while (true) {
    const expense = prompt("Enter expense amount (or 'done' to finish): ");
    if (expense.toLowerCase() === "done") {
      trackIncome();
      break;
    }

    const expenseAmount = parseFloat(expense);
    if (isNaN(expenseAmount) || expenseAmount <= 0) {
      console.log("Invalid expense amount. Please enter a valid number.");
      continue;
    }

    expenses.push(expenseAmount);
    totalSpent += expenseAmount;
    if (totalSpent >= 3000) {
      trackIncome();
      break;
    }
  }
}

// Function to track income
function trackIncome() {
  while (true) {
    const incomeEarned = prompt("Enter income earned (or 'done' to finish): ");
    if (incomeEarned.toLowerCase() === "done") {
      displayFinances();
      break;
    }

    const incomeAmount = parseFloat(incomeEarned);
    if (isNaN(incomeAmount) || incomeAmount <= 0) {
      console.log("Invalid income earned. Please enter a valid number.");
      continue;
    }

    income.push(incomeAmount);
  }
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
