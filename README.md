# Powerball Strategy Model (2025)

A Python-based statistical lottery tool designed to generate "Smart Picks" for the Powerball. Instead of simple random guessing, this model uses **Heuristic Filtering** and **Prize-Protection** logic to select numbers that mirror historical winning patterns while avoiding over-played human sequences.

## Strategic Filters Included
To maximize potential payout and follow the **Law of Large Numbers**, every generated play must pass these six filters:

*   **Sum Analysis:** Total value of white balls is kept between **130–180** (the historical "Bell Curve" sweet spot).
*   **High-Low Balance:** Ensures a **2:3 or 3:2 split** between low (1-34) and high (35-69) numbers.
*   **Odd-Even Balance:** Prevents all-odd or all-even sets to mirror natural mechanical randomness.
*   **Multiples Protection:** Discards sets that follow mathematical patterns (e.g., 5, 10, 15...) to avoid splitting jackpots with other players.
*   **Last Digit Filter:** Prevents "clumping" by ensuring no more than two numbers end in the same digit (e.g., avoids 4, 14, 24).
*   **Post-Birthday Filter:** Requires at least **3 numbers abo
