use std::io;

fn main() {
    // Read the first number
    let num1: f64 = get_user_input("Enter the first number:");

    // Read the operator
    let operator: char = get_user_input("Enter the operator (+, -, *, /):");

    // Read the second number
    let num2: f64 = get_user_input("Enter the second number:");

    // Perform the calculation based on the operator
    let result = match operator {
        '+' => num1 + num2,
        '-' => num1 - num2,
        '*' => num1 * num2,
        '/' => {
            if num2 != 0.0 {
                num1 / num2
            } else {
                println!("Error: Division by zero!");
                return;
            }
        }
        _ => {
            println!("Error: Invalid operator!");
            return;
        }
    };

    // Display the result
    println!("Result: {}", result);
}

// Function to get user input and parse it as f64
fn get_user_input(prompt: &str) -> f64 {
    loop {
        println!("{}", prompt);

        let mut input = String::new();
        io::stdin().read_line(&mut input).expect("Failed to read line");

        match input.trim().parse() {
            Ok(num) => return num,
            Err(_) => println!("Invalid input. Please enter a valid number."),
        }
    }
}
