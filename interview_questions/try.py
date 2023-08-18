from pathlib import Path


def main():

    p = Path(__file__).with_name("sample.log")

    with p.open('r') as f:
        # print(f.read())
        count = 0
        for ln in f:
            count += 1
        
            split = ln.split(' ')
            print(split)

            for p in s:
                
    
        print(count)

main()