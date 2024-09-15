file=open("quotes.txt","r")
lines = file.split("\n")
def ReadIndex(line):
    quote = line.split("\\")[0]
    reason = line.split("\\")[1]
    subquote = line.split("\\")[2]
    short = line.split("\\")[3]
    significance = line.split("\\")[4]
    print(f"Quote: {quote}")
    print(f"Short: {short}")
    print(f"Reason: {reason}")
    print(f"Subquote: {subquote}")
    
    print(f"Significance: {significance}")
ReadIndex(lines[0])