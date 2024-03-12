
cost_seatA = 20
cost_seatB = 15
cost_seatC = 10

def main():
    numSeatA , numSeatB, numSeatC = int(input("please enter the number of seat for A, B, AND C: ").split())
    incomeGen = income_gen(numSeatA, numSeaatB, numSeatC)
    print(f"Income generated is{incomeGen}");

def income_gen(numSeatA, numSeatB, numSeatC):
    return ((numSeatA * cost_seatA) + (numSeatB * cost_seatA) + (numSeatC * cost_seatC))

main()
