# Ask the operator what he wants to do.

def logo():
	print("""\

	     _______.____    ____  _______. __       _______ .__   __.      _______.         ______  __       __  
	    /       |\   \  /   / /       ||  |     |   ____||  \ |  |     /       |        /      ||  |     |  | 
	   |   (----` \   \/   / |   (----`|  |     |  |__   |   \|  |    |   (----` ______|  ,----'|  |     |  | 
	    \   \      \_    _/   \   \    |  |     |   __|  |  . `  |     \   \    |______|  |     |  |     |  | 
	.----)   |       |  | .----)   |   |  `----.|  |____ |  |\   | .----)   |          |  `----.|  `----.|  | 
	|_______/        |__| |_______/    |_______||_______||__| \__| |_______/            \______||_______||__| 


	""")
	print("Welcome to Syslens-CLI: What do you want to do?:")


def menu():
	print("""
	1. Verify container status and health
	2. Check System performance and Disk Space
	0. Exit
	""")
	answer = int(input("1, 2 or 0: "))
	return answer
