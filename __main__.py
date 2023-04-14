import sys
import pathlib
from site_check import site_is_online
from cli import display_check_result,read_user_cli_args

def main():
    """Run site checker"""
    user_args = read_user_cli_args()
    urls = user_args.urls
    if not urls:
        print("No URLs for analysis",file=sys.stderr)
        sys.exit(1)
    _site_check(urls)
    
def _site_check(urls):
    for url in urls:
        error = ""
        try:
            result = site_is_online(urls)
        except Exception as e:
            result = False
            error = str(e)
            display_check_result(result,url,error)
if __name__ == '__main__':
    main()