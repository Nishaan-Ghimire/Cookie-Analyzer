import argparse
import requests
import pyfiglet 
import time


# Takes the file and extract all key of cookies and save in a output file
def extract_cookies(input_file, output_file):
    with open(input_file, 'r') as file:
        cookies = file.read()

    cookie_list = cookies.split(';')
    
    with open(output_file, 'w') as out_file:
        for i, cookie in enumerate(cookie_list, 1):
            cookie_name = cookie.split('=')[0]
            out_file.write(f"{i}. {cookie_name}\n")



# Not completed function --> Request the url for getting cookie and save the output in a file
def urlCookieExtractor(url,output_file):

    url = 'https://booking.com'
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    }
    response = requests.get(url, headers=headers)
    cookies = response.cookies

def analyzeCookie(input_file,output_file):
    with open(input_file, 'r') as file:
        cookies = file.read()
    # print(cookies)
    cookie_list = cookies.split('\nCookie:');
    cookie_list_one = cookie_list[0].replace('Cookie:','');
    cookie_list_two = cookie_list[1];
    # print(cookie_list_two)
    cookie_list_one_param = cookie_list_one.split(';')
    cookie_list_two_param = cookie_list_two.split(';')
    # print(cookie_list_two_param)
    cookie_param_ones = [cookie.split('=')[0] for cookie in cookie_list_one_param]
    cookie_param_twos = [cookie.split('=')[0] for cookie in cookie_list_two_param]
    # print(cookie_param_ones)
    # print(cookie_param_twos)

    added_parameters = set(cookie_param_twos) - set(cookie_param_ones)
    removed_parameters = set(cookie_param_ones) - set(cookie_param_twos)
    unchanged_parameters = set(cookie_param_ones) & set(cookie_param_twos)
    with open(output_file, 'w') as out_file:
        print("----------------------------------Result------------------------------------")
        out_file.write("-----------------------------Result------------------------------------")
        print("Added Cookie parameters:")
        out_file.write('\nAdded Cookie parameters:\n')
        for param in added_parameters:
            out_file.write('\n')
            out_file.write(param)
            out_file.write('\n')
            print(param)
        print("-----------------------------------------------------------------------------")
        print("\nRemoved Cookie parameters:")
        out_file.write('\nRemoved Cookie parameters:\n')
        for param in removed_parameters:
            out_file.write(param)
            out_file.write('\n')
            print(param)
        print("-----------------------------------------------------------------------------")
        print("\nUnchanged parameters:")
        out_file.write('\nUnchanged parameters:\n')
        for param in unchanged_parameters:
            out_file.write(param)
            out_file.write('\n')
            print(param)
        print("-----------------------------------------------------------------------------")
       


if __name__ == "__main__":
    title = pyfiglet.figlet_format("Cookie-Analyzer")
    print(title)
    print("Developed by @nishan")
    print("Example uses : python3 cookie-extractor.py -i input.txt -o output.txt")
    print("Note : Keep the both input cookie in one file separate by a line")
    time.sleep(5)

    parser = argparse.ArgumentParser(description='Cookie Parameter Extractor')
    parser.add_argument('-i', '--input', help='Input file containing the cookie string', required=True)
    parser.add_argument('-o', '--output', help='Output file for extracted cookie parameters', required=False)
    parser.add_argument('-u','--url',help='URL in https://example.com',required=False)
    
    # parse.add_argument('-A','--Analyze',help='Analyze the cookie',required=False)
    args = parser.parse_args()
    analyzeCookie(args.input,args.output)       
    # extract_cookies(args.input, args.output)



