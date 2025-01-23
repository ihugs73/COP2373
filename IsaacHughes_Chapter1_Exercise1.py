# Cinema Ticket Pre-Sale Application
# This program allows users to pre-purchase cinema tickets with a maximum of 20 tickets available.
# Each buyer can buy up to 4 tickets. The program displays the remaining tickets after each purchase
# and tracks the total number of buyers.

# Constant for the total number of tickets
TOTAL_TICKETS = 20


def get_ticket_request(remaining_tickets):
    """
    Prompts the user for the desired number of tickets.
    Ensures the user does not request more tickets than allowed or available.
    """
    while True:
        try:
            # Prompt user for ticket request
            tickets_requested = int(
                input(f"Enter the number of tickets you'd like to buy (up to 4, {remaining_tickets} available): "))

            # Validate input
            if 1 <= tickets_requested <= 4 and tickets_requested <= remaining_tickets:
                return tickets_requested
            else:
                print(
                    f"Invalid input. You can only buy up to 4 tickets, and no more than the {remaining_tickets} available.")
        except ValueError:
            print("Invalid input. Please enter a whole number between 1 and 4.")


def ticket_sales():
    """
    Handles the ticket sale process, displaying the number of tickets remaining
    and counting the number of buyers.
    """
    remaining_tickets = TOTAL_TICKETS
    total_buyers = 0

    while remaining_tickets > 0:
        # Get the number of tickets requested by the buyer
        tickets_requested = get_ticket_request(remaining_tickets)

        # Update the number of remaining tickets
        remaining_tickets -= tickets_requested

        # Increment the total number of buyers
        total_buyers += 1

        # Display the number of tickets remaining
        print(f"Tickets sold: {tickets_requested}. Tickets remaining: {remaining_tickets}.")

    # Display the total number of buyers
    print(f"All tickets have been sold! Total buyers: {total_buyers}.")


# Run the ticket sales process
if __name__ == "__main__":
    ticket_sales()

