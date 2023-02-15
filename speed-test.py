# All th things needed to run this project. 
## Don't remove.
import speedtest
from rich import print

print("    ")
print("[bold red]-------------------------------------------------------------")
print("    ")
print("[bold red]Keep in Mind, Internet speed chnage so much that these results may not be as accurate as a speed test site.")
print("    ")
print("[bold red]-------------------------------------------------------------")
print("    ")
print("[bold blue]Running SpeedTest")
test = speedtest.Speedtest()
download = test.download()
upload = test.upload()
print("[bold green]|----------------------------------|")
print(f"[bold green]|Download Speed | {download}")
print(f"[bold green]|Upload Speed   | {upload}")
print("[bold green]|----------------------------------|")
