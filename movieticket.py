class MovieTicketBooking:
    def __init__(self):
        self.movies = {
            "1": {"name": "Avengers: Endgame", "seats": 50, "price": 250},
            "2": {"name": "Interstellar", "seats": 40, "price": 200},
            "3": {"name": "Inception", "seats": 30, "price": 220},
        }
        self.bookings = []

    def display_movies(self):
        print("Available Movies:")
        for key, movie in self.movies.items():
            print(f"{key}. {movie['name']} - Seats Available: {movie['seats']} - Price: Rs.{movie['price']}")

    def book_ticket(self):
        self.display_movies()
        choice = input("Enter the movie number you want to book: ")
        if choice in self.movies:
            movie = self.movies[choice]
            num_seats = int(input("Enter number of seats: "))
            if num_seats <= movie['seats']:
                total_price = num_seats * movie['price']
                confirm = input(f"Total price is Rs.{total_price}. Confirm booking? (yes/no): ")
                if confirm.lower() == "yes":
                    movie['seats'] -= num_seats
                    self.bookings.append({"movie": movie['name'], "seats": num_seats, "price": total_price})
                    print("Booking confirmed!")
                else:
                    print("Booking cancelled.")
            else:
                print("Not enough seats available.")
        else:
            print("Invalid choice.")

    def view_bookings(self):
        if not self.bookings:
            print("No bookings made yet.")
        else:
            print("Your Bookings:")
            for booking in self.bookings:
                print(f"Movie: {booking['movie']}, Seats: {booking['seats']}, Total Price: Rs.{booking['price']}")

if __name__ == "__main__":
    app = MovieTicketBooking()
    while True:
        print("\n1. View Movies\n2. Book Ticket\n3. View Bookings\n4. Exit")
        option = input("Enter your choice: ")
        if option == "1":
            app.display_movies()
        elif option == "2":
            app.book_ticket()
        elif option == "3":
            app.view_bookings()
        elif option == "4":
            print("Thank you for using the Movie Ticket Booking system!")
            break
        else:
            print("Invalid option. Please try again.")
