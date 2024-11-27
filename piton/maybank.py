class LoanCalculator:
    def __init__(self, name, ic_number, amount, salary):
        self.name = name
        self.ic_number = ic_number
        self.amount = amount
        self.salary = salary

    def calculate_loan_eligibility(self):
        if self.amount < 100000:
            if self.salary > 8000:
                loan = self.amount
            elif self.salary > 5000:
                loan = self.amount * 0.7
            elif self.salary > 3000:
                loan = self.amount * 0.5
            else:
                loan = self.amount * 0.3
        else:
            loan = 0.00
        return loan

    def display_loan_status(self):
        print("ABC BANK LOAN")
        print(f"Applicant Name: {self.name}")
        print(f"IC Number: {self.ic_number}")
        print()
        loan = self.calculate_loan_eligibility()
        if loan > 0:
            print(f"Loan eligibility (RM): {loan:.2f}")
            print("Congrats, you are eligible to apply for a loan.")
        else:
            print(f"Loan eligibility (RM): {loan:.2f}")
            print("Sorry!!! Your amount request is over the limit. Thank you.")

def calcfactory(name, ic_number, amount, salary):
    return LoanCalculator(name, ic_number, amount, salary)

if __name__ == "__main__":
    try:
        name = input("Enter your name: ")
        ic_number = input("Enter your IC number: ")
        amount = float(input("Enter the loan amount (RM): "))
        salary = float(input("Enter your monthly salary (RM): "))
        loan_calculator = calcfactory(name, ic_number, amount, salary)
        loan_calculator.display_loan_status()
    except ValueError:
        print("Invalid input! Please enter numeric values for amount and salary.")