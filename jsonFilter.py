import json
import os

input_file = "yelp_academic_dataset_business.json"
output_file = "yelp_filtered_to_santa_barbara.json"

def main():
    '''Opens the input_file and runs the line filter on each line then write it to another json file'''
    linesTotal = 0
    linesKept = 0
    if os.path.exists(output_file):
        print("Removing previous output file")
        os.remove(output_file)
    with open(output_file, 'a', encoding='utf-8') as outFile:
        with open(input_file, 'r', encoding='utf-8') as inFile:
            for line in inFile:
                linesTotal+=1
                # Write which rows to write to output filter
                parseLine = filterBySantaBarbara(line)
                if parseLine is not None:
                    linesKept+=1
                    # print(parseLine)
                    outFile.write(parseLine)
    print("{} is ({}/{}) = {:.2f}% of the lines that were in {}".format(output_file,linesKept,linesTotal,linesKept/linesTotal,input_file))

def filterBySantaBarbara(line):
    '''This function is run on every line of the input dataset
    If the business is within the greater santa barbara area return it'''
    jsonLine = json.loads(line)
    # Check that the city is santa barbara and santity check the state
    if 'barbara' in jsonLine['city'].lower() and 'ca' in jsonLine['state'].lower():
        print(jsonLine['name'])
        return json.dumps(jsonLine)+'\n'
    else:
        return None

if __name__ == '__main__':
    main()