
def caught_speeding(speed, is_birthday):
    if is_birthday:
        speeding = speed - 5
    else:
        speeding = speed

    if speeding > 80:
        return 'Big Ticket'
    elif speeding > 60:
        return 'Small ticket'
    else:
        return 'No Ticket'


fine = caught_speeding(81, True)
print(fine)
