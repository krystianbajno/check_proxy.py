from check_proxy.core.colors import Colors

def display_banner():
    banner = f"""{Colors.GREEN}
       _               _                                                
      | |             | |                                               
   ___| |__   ___  ___| | __    _ __  _ __ _____  ___   _   _ __  _   _ 
  / __| '_ \\ / _ \\/ __| |/ /   | '_ \\| '__/ _ \\ \\/ / | | | | '_ \\| | | |
 | (__| | | |  __/ (__|   <    | |_) | | | (_) >  <| |_| |_| |_) | |_| |
  \\___|_| |_|\\___|\\___|_|\\_\\   | .__/|_|  \\___/_/\\_\\\\__, (_) .__/ \\__, |
                         ______| |                   __/ | | |     __/ |
                        |______|_|                  |___/  |_|    |___/ 
{Colors.RESET}
                                                       Krystian Bajno 2018
Contributors:                                                      {Colors.CYAN}{Colors.BOLD}v2 2024{Colors.RESET}
{Colors.VIOLET}{Colors.BOLD}@Artideusz{Colors.RESET} {Colors.CYAN}(https://github.com/Artideusz){Colors.RESET}
   """
    print(banner)