#Problem Statement

make a two-part Python script that first generates a simple user ID combining a given name with four random digits, and then generates a separate password where the user specifies the length and chooses the complexity from three options: Letters, Letters + Numbers, or Letters + Numbers + Symbols. What is the code?

#Scope of the Project

The scope of this project is to provide a foundational, two-stage credential generator. Its functions are:
1.Generating a basic user ID using the user's name and a 4-digit random number suffix.
2.Creating a password with customizable length and character complexity (letters, numbers, and symbols).

#Targeted Users

Targeted users for this simple credential generator are beginners who are learning Python, individuals needing a temporary/placeholder credentials for development or testing environments, and the users requiring a quick, random, customizable passwords without needing advanced security features like entropy scoring, persistence, or unique character guarantees.

#Features

1.Personalized ID Generation: The system allows the user's first name directly into the ID format (e.g., Name@Random Digits),it will make the output more relevant than a purely random string.
2.Random Number Suffix: It will automatically add a 4-digit random number to the name portion of the ID, for creating uniqueness across different users.
3.Custom Password Length: Users have control over the strength of their password by specifying the exact number of characters they required.

4.Three Complexity Tiers: This password generator has three clear complexity options: Letters only (L), Letters and Numbers (LN), and for maximum security Letters, Numbers, and Symbols (LNS).
