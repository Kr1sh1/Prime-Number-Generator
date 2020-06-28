candidates = list(range(2, int(input("Enter the number you'd like to search up to: ")) + 1))
primes = []

while len(candidates) > 0:
    prime = candidates[0]
    primes.append(prime)
    for candidate in candidates:
        if candidate % prime == 0:
            candidates.remove(candidate)

primes = list(map(str, primes))

if input("Save generated primes to csv text file? (y/n)").lower() == "y":
    save_file_name = input("Enter save file name: ")
    with open(save_file_name, "w") as save_file:
        save_file.write(",".join(primes))