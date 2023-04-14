import argparse

def read_user_cli_args():
    parser = argparse.ArgumentParser(
        prog="site_checker",description='checking if a URL is online'    
    )
    parser.add_argument(
        "-u",
        "--urls",
        metavar='URLs',
        nargs='+',
        type=str,
        default=[],
        help="Insert one or more URLs"
    )
    return parser.parse_args()

def display_check_result(result, url, error=""):
    """Display the result of a connectivity check."""
    print(f'"{url}"status is:', end=" ")
    if result:
        print('"Online!" 👍')
    else:
        print(f'"Offline?" 👎 \n  Erro: "{error}"')