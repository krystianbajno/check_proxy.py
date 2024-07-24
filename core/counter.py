from threading import Lock
from core.colors import Colors

def create_counter():
    return {
        'working': 0,
        'progress': 0,
        'total': 0,
        'lock': Lock()
    }

def add_working(counter):
    with counter['lock']:
        counter['working'] += 1

def add_progress(counter):
    with counter['lock']:
        counter['progress'] += 1

def set_total(counter, total):
    counter['total'] = total

def get_progress(counter):
    return counter['progress']

def get_total(counter):
    return counter['total']

def get_working(counter):
    return counter['working']

def print_progress(counter, line):
    print(f"{Colors.GREEN}{get_working(counter)} WORKING{Colors.RESET} - {get_progress(counter)}/{get_total(counter)} - trying {Colors.CYAN}{line}{Colors.RESET}")
