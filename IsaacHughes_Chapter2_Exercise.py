def scan_message(message, keywords):
    """
    Scans the message for each keyword/phrase in the keywords list.
    Returns the total spam score and a list of (keyword, count) tuples for those found.
    """
    message_lower = message.lower()  # make search case-insensitive
    score = 0
    found_keywords = []  # will hold tuples of (keyword, count)

    for keyword in keywords:
        # Count how many times the keyword appears in the message.
        # Using .count() works for both words and phrases.
        count = message_lower.count(keyword.lower())
        if count > 0:
            score += count
            found_keywords.append((keyword, count))

    return score, found_keywords


def determine_spam_likelihood(score):
    """
    Returns a text message indicating the likelihood that the email is spam,
    based on the spam score.
    """
    if score == 0:
        return "Not spam"
    elif score < 5:
        return "Possibly not spam"
    elif score < 10:
        return "Likely spam"
    else:
        return "Definitely spam"


def main():
    # List of 30 common spam keywords and phrases.
    spam_keywords = [
        "free", "winner", "win", "money", "cash", "prize", "urgent", "act now",
        "limited time", "guarantee", "risk-free", "offer", "click here", "order now",
        "buy now", "special promotion", "discount", "cheap", "no cost", "earn extra cash",
        "investment", "miracle", "work from home", "credit card", "luxury", "congratulations",
        "exclusive deal", "cash bonus", "lottery", "unsubscribe"
    ]

    # Get the email message from the user.
    email_message = input("Enter your email message:\n")

    # Scan the message for spam keywords.
    score, found_keywords = scan_message(email_message, spam_keywords)

    # Determine spam likelihood based on score.
    likelihood = determine_spam_likelihood(score)

    # Display the results.
    print("\n--- Spam Analysis ---")
    print(f"Spam Score: {score}")
    print(f"Spam Likelihood: {likelihood}")

    if found_keywords:
        print("\nSpam keywords/phrases found:")
        for keyword, count in found_keywords:
            # Handle singular vs. plural
            times = "time" if count == 1 else "times"
            print(f"  '{keyword}' found {count} {times}")
    else:
        print("No spam keywords or phrases were detected in the message.")


# Run the main function if this script is executed.
if __name__ == "__main__":
    main()
