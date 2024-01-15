
if __name__ == '__main__':
    # Input the number of participants
    n = int(input())

    # Input the array of scores
    scores = list(map(int, input().split()))

    # Sort the scores in descending order
    sorted_scores = sorted(scores, reverse=True)

    # Find the unique runner-up score
    runner_up_score = None
    for score in sorted_scores:
        if score < max(sorted_scores):
            runner_up_score = score
            break

    # Print the runner-up score
    print(runner_up_score)