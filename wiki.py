import datetime

answer_format = '%m/%d'
link_format = '%b_%d'
link = 'http://en.wikipedia.org/wiki/{}'

while True:
    answer = input("Enter a date in MM/DD format or 'quit' to exit: ")
    if answer.upper() == 'QUIT':
        break

    try:
        date = datetime.datetime.strptime(answer, answer_format)
        output = link.format(date.strftime(link_format))
        print(output)
    except ValueError:
        print("Bad format, try again")
