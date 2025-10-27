def main():
    try:
        top_artists = ["The Beatles", "Madonna", "Elton John", "Elvis Presley",
                   "Mariah Carey", "Stevie Wonder", "Janet Jackson",
                   "Michael Jackson", "Whitney Houston", "Rihanna"]
    
        print("Current artists:", top_artists)

        index = int(input("Enter the artist name you want to replace (0-9): "))
        new_name = input("Enter the new artist name: ")

        top_artists[index] = new_name

        print("updated artists list:")
        print(top_artists)

    except (ValueError, TypeError, IndexError) as e:
        print(f"an error acured please try again: {e}")
main()
    