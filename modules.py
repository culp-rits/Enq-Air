import sys, hashlib, getpass                                                                #importing required libraries

#hash - sha256 hashing function using python library - hashlib used to encrypt password before storing

class hash:                                                                                 #defining class hash

    def __init__(self,data):
        self.hash_value = hashlib.sha256(data.encode())                                     #sha256 hashing function
    
    def get_hash(self):
        return self.hash_value.hexdigest()                                                  #returns hashvalue to authorize login 

#hashtable - stores all the user accounts after encryption, perform operations in O(1), O(n)

class hashtable:
    
    def __init__(self):
        self.table = {}                                                                     #table stores all the accounts
    
    def add(self,data):
        self.table[data.password] = data                                                    #using password as key and name as value, adding new users

    def get(self,data):
        return self.table.get(data)                                                         #returns the password for the requested user

    def show(self):                                                                         #prints all the usernames
        for i in self.table:
            print("\t",self.table[i].name)                                                  

#queue - used along with djikstra algorithm to find the route taken to the destination

class queue:
    
    def __init__(self):
        self.q = []                                                                         #q stores the cities in a specific order
    
    def enqueue(self,data):                                                                 #adding new city to the queue
        self.q.append(data)
    
    def dequeue(self):                                                                      #return the next city to be travelled
        if(self.empty() != True):
            return self.q.pop(0)
    
    def empty(self):                                                                        #returns if the queue is empty
        return self.q == []

#splaytree - used to store the admin user details as it suits the data structure property more 

class splaytree:

    def __init__(self):                                                                     #initalizing root node
        self.root = None

    def zag(self, x):                                                                       #node left rotation
        y = x.right
        x.right = y.left
        if y.left != None:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def zig(self, x):                                                                       #node right rotation
        y = x.left
        x.left = y.right
        if y.right != None:
            y.right.parent = x
        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y
    
    def zigzig(self,p,g):                                                                   #node right-right rotation
        self.zig(g)
        self.zig(p)

    def zagzag(self,p,g):                                                                   #node left-left rotation
        self.zag(g)
        self.zag(p)
    
    def zagzig(self,p,g):                                                                   #node right-left rotation
        self.zag(p)
        self.zig(g)
    
    def zigzag(self,p,g):                                                                   #node left-right rotation
        self.zig(p)
        self.zag(g)

    def splay(self, n):                                                                     #splaying the node to the root
        while (n.parent != None):
            if (n.parent == self.root):
                if (n == n.parent.left):
                    self.zig(n.parent)
                else:
                    self.zag(n.parent)
            else:
                p = n.parent
                g = p.parent
                if (n.parent.left == n and p.parent.left == p):
                    self.zigzig(p,g)
                elif (n.parent.right == n and p.parent.right == p):
                    self.zagzag(p,g)
                elif (n.parent.right == n and p.parent.left == p):
                    self.zagzig(p,g)
                elif (n.parent.left == n and p.parent.right == p):
                    self.zigzag(p,g)

    def insert(self, n):                                                                    #inserting new eletment to the tree
        y = None
        temp = self.root
        while (temp != None):
            y = temp
            if (n.name < temp.name):
                temp = temp.left
            else:
                temp = temp.right
        n.parent = y
        if (y == None):
            self.root = n
        elif (n.name < y.name):
            y.left = n
        else:
            y.right = n
        self.splay(n)

    def Search(self, n, x):                                                                 #searching for a user in the tree 
        if(n != None):
            if (x.name == n.name):
                self.splay(n)
                return n
            elif (x.name < n.name):
                return self.Search(n.left, x)
            elif (x.name > n.name):
                return self.Search(n.right, x)
        else:
            return None
    
    def show(self,root):                                                                    #printing all the admin users
        if(root != None):
            print("\t",root.name)
            admins.show(root.left)
            admins.show(root.right)

#graph - stores the cities, flight details as adjacency matrix and uses djikstra for computation

class graph:
    
    def __init__(self):
        self.w_dist = [[0,79,0,34,0,0,87,0,74,21],                                          #distance between two airports
                       [0,0,26,0,69,92,0,17,24,0],
                       [38,0,0,0,32,0,99,14,0,63],
                       [25,47,53,0,0,31,0,0,0,42],
                       [0,59,0,42,0,46,0,37,0,39],
                       [27,82,0,0,49,0,0,58,0,33],
                       [62,0,93,28,0,23,0,0,29,0],
                       [19,0,29,0,51,0,59,0,28,0],
                       [0,23,46,0,82,52,61,0,0,0],
                       [14,0,0,37,0,0,53,65,79,0]]                                              
        self.w_time = [[0,3,0,2,0,0,4,0,4,3],                                               #flight time duration
                       [0,0,2,0,4,5,0,1,2,0],
                       [4,0,0,0,4,0,5,1,0,3],
                       [2,3,2,0,0,3,0,0,0,3],
                       [0,3,0,2,0,2,0,2,0,3],
                       [2,5,0,0,2,0,0,3,0,2],
                       [3,0,5,2,0,2,0,0,2,0],
                       [1,0,2,0,3,0,3,0,2,0],
                       [0,2,3,0,4,3,3,0,0,0],
                       [1,0,0,2,0,0,3,3,4,0]]
        self.w_cost = [[0,39,0,17,0,0,45,0,36,10],                                          #Flight ticket cost 
                       [0,0,13,0,35,46,0,8,12,0],
                       [19,0,0,0,16,0,50,7,0,32],
                       [13,24,26,0,0,16,0,0,0,19],
                       [0,29,0,20,0,23,0,19,0,16],
                       [14,41,0,0,25,0,0,30,0,17],
                       [32,0,49,14,0,11,0,0,15,0],
                       [10,0,15,0,26,0,29,0,13,0],
                       [0,12,23,0,40,25,31,0,0,0],
                       [7,0,0,18,0,0,24,31,38,0]]
        self.name = ["Berlin ","Rio    ","Tokyo  ","Moscow ","Denver ",                     #list of all city names
        "Stockholm","Lisbon","Palermo","Helsinki","Nairobi"]
        self.dist = []                                                                      #shortest path computed matrix for all combination of flight routes                                                     
        self.time = []                                                                      #fastest path computed matrix for all combination of flight routes
        self.cost = []                                                                      #cheapest path computed matrix for all combination of flight routes
        self.p_dist = []                                                                    #will contain computed least distance path
        self.p_time = []                                                                    #will contain computed fastest path                       
        self.p_cost = []                                                                    #will contain computed cheapest path
        self.compute()                                                                      #to compute

    def min_cal(self,val,adj):                                                              #finding closest value neighbour
        min=sys.maxsize
        for i in range(10):
            if (val[i] < min and adj[i] == False):
                min = val[i]
                min_index = i
        return min_index

    def djikstra(self,val,i):                                                               #djikstra shortest path algorithm 
        sol = [sys.maxsize]*10
        sol[i] = 0
        adj = [False]*10
        p = [-1]*10
        for j in range(10):
            x = self.min_cal(sol,adj)
            adj[x] = True
            for k in range(10):
                if(val[x][k] > 0 and adj[k] == False and sol[k] > sol[x]+val[x][k]):        
                    sol[k] = sol[x]+val[x][k]
                    p[k] = x
        return [sol,p]

    def compute(self):                                                                      #computes fastest, nearest, cheapest paths
        for i in range(10):
            x = self.djikstra(self.w_dist,i)
            self.dist.append(x[0])
            self.p_dist.append(x[1])
        for i in range(10):
            x = self.djikstra(self.w_time,i)
            self.time.append(x[0])
            self.p_time.append(x[1])
        for i in range(10):
            x = self.djikstra(self.w_cost,i)
            self.cost.append(x[0])
            self.p_cost.append(x[1])

    def add_route(self,src,dst,dist,dur,pri):                                               #adding new route
        self.dist.clear()
        self.cost.clear()
        self.time.clear()
        self.p_dist.clear()
        self.p_time.clear()
        self.p_cost.clear()
        self.w_cost[src-1][dst-1]=pri
        self.w_time[src-1][dst-1]=dur
        self.w_dist[src-1][dst-1]=dist
        self.compute()                                                                      #computes new path

    def del_route(self,src,dst):                                                            #deleting existing route
        self.dist.clear()
        self.cost.clear()
        self.time.clear()
        self.p_dist.clear()
        self.p_time.clear()
        self.p_cost.clear()
        self.w_cost[src-1][dst-1]=0
        self.w_time[src-1][dst-1]=0
        self.w_dist[src-1][dst-1]=0
        self.compute()                                                                      #computes new route

    def set_route(self,src,dst,dist,dur,pri):                                               #changing existing route
        self.dist.clear()
        self.cost.clear()
        self.time.clear()
        self.p_dist.clear()
        self.p_time.clear()
        self.p_cost.clear()
        self.w_cost[src-1][dst-1]=pri
        self.w_time[src-1][dst-1]=dur
        self.w_dist[src-1][dst-1]=dist
        self.compute()                                                                      #computes new path

    def cities(self):                                                                       #prints the list of cities
        print("\n\tC I T I E S\n")
        for i in range(10):
            print("\t",i+1,"\t",self.name[i])
    
    def add_menu(self):                                                                     #add route menu
        x = []
        print("\n\tA D D    R O U T E")
        route.cities()
        x.append(int(input("\n\t\tEnter Source  : ")))
        x.append(int(input("\t\tEnter Destination : ")))
        x.append(int(input("\t\tEnter Distance  : ")))
        x.append(int(input("\t\tEnter Time : ")))
        x.append(int(input("\t\tEnter Cost  : ")))
        return x

    def del_menu(self):                                                                     #delete route menu
        x = []
        print("\n\tD E L E T E    R O U T E")
        route.cities()
        x.append(int(input("\n\t\tEnter Source  : ")))
        x.append(int(input("\t\tEnter Destination : ")))
        return x
    
    def set_menu(self):                                                                     #set route menu
        x = []
        print("\n\tS E T    R O U T E")
        route.cities()
        x.append(int(input("\n\t\tEnter Source  : ")))
        x.append(int(input("\t\tEnter Destination : ")))
        x.append(int(input("\t\tEnter Distance  : ")))
        x.append(int(input("\t\tEnter Time : ")))
        x.append(int(input("\t\tEnter Cost  : ")))
        return x

    def time_menu(self):                                                                    #returns the list of cities in fastest route
        x = []
        print("\n\tF A S T E S T    R O U T E")
        route.cities()
        x.append(int(input("\n\t\tFrom : ")))
        x.append(int(input("\t\tTo : ")))
        return x

    def cost_menu(self):                                                                    
        x = []
        print("\n\tC H E A P E S T    R O U T E")                                           #returns the list of cities in the cheapest route
        route.cities()
        x.append(int(input("\n\t\tFrom : ")))
        x.append(int(input("\t\tTo : ")))
        return x
    
    def menu(self):                                                                         #view graph menu
        print("\n\tM E N U")
        print("\n\t\t1 - Distance Graph")
        print("\t\t2 - Time Graph")
        print("\t\t3 - Cost Graph")
        return int(input("\n\t\tEnter Choice : "))

    def get_flight_t(self,list,src,dst):                                                    #stores the flight details of fastest route
        if(self.p_time[src][dst] == -1):
            list.append(dst)
            return
        self.get_flight_t(list,src,self.p_time[src][dst])
        list.append(dst)
    
    def get_flight_c(self,list,src,dst):                                                    #stores the flight details of cheapest route
        if(self.p_cost[src][dst] == -1):
            list.append(dst)
            return
        self.get_flight_c(list,src,self.p_cost[src][dst])
        list.append(dst)

    def show_dist(self):                                                                    #view distance graph
        print("\n\tD I S T A N C E")
        for i in self.w_dist:
            print("\n\t\t",end = "")
            for j in i:
                print(j,end = " ")
        print("\n")

    def show_time(self):                                                                    #view time graph
        print("\n\tT I M E")
        for i in self.w_time:
            print("\n\t\t",end = "")
            for j in i:
                print(j,end = " ")
        print("\n")

    def show_cost(self):                                                                    #view cost graph
        print("\n\tC O S T")
        for i in self.w_cost:
            print("\n\t\t",end = "")
            for j in i:
                print(j,end = " ")
        print("\n")

    def print_route(self,list):                                                             #prints flight details
        t = 0
        c = 0
        flights = queue()
        for i in range(len(list)-1):
            flights.enqueue(flight(list[i],list[i+1]))
        print("\n\tR O U T E")
        print("\n\t\tFlight\t\t From\t\t To\t\t Time\t Cost\n")
        while(flights.empty() != True):
            f = flights.dequeue()
            print("\t\tFlight",str(f.src)+str(f.dst),"\t",route.name[f.src-1],"\t",
            route.name[f.dst-1],"\t",f.time,"hrs\t $",f.cost,end=",000\n")
            t += f.time
            c += f.cost
        print("\n\t\tDuration :",t,end="hrs")
        print("\t\tCost : $",c,end =",000\n")

    def print_from(self,x):                                                                 #prints available flights from
        for i in range(10):
            if(self.w_dist[x-1][i] != 0):
                print("\t\t",self.name[i])    

    def print_to(self,x):                                                                   #prints available flights to
        for i in range(10):
            if(self.w_dist[i][x-1] != 0):
                print("\t\t",self.name[i])

    def get_dist(self,src,dst):                                                             #returns distance
        return self.w_dist[src][dst]
    
    def get_time(self,src,dst):                                                             #returns time
        return self.w_time[src][dst]
    
    def get_cost(self,src,dst):                                                             #returns cost
        return self.w_cost[src][dst]

#admin - stores the admin login details and has all the functionalities of admin user

class admin:

    def __init__(self,name,password):                                                       #admin details in form of splay tree
        self.admin_pw=hash("F1").get_hash()
        self.name=name
        self.password=hash(password).get_hash()
        self.right = None
        self.left = None
        self.parent = None

    def login(self):                                                                        #admin login function
        print("\n\tL O G I N")
        name = input("\n\t\tEnter Name : ")
        password = getpass.getpass(prompt="\t\tEnter Password : ")
        if (self.authenticate(name,password)==True):
            self.func()
        else:
            x = self.invalid_menu()
            if (x==1):
                self.login()
            elif (x==2):
                self.create_acc()
    
    def create_acc(self):                                                                   #creates new admin login
        if(self.admin_auth()==True):
            print("\n\tC R E A T E    A C C O U N T")
            admins.insert(admin(input("\n\t\tEnter Name : "),
            getpass.getpass(prompt="\t\tEnter Password : ")))
            self.login()
        else:
            self.login()

    def admin_auth(self):                                                                   #admin password authentication function
        password=hash(getpass.getpass(prompt="\n\t\tEnter Admin Password : ")).get_hash()
        if (password==self.admin_pw):
            return True
        else:
            return False

    def authenticate(self,name,password):                                                   #admin login authentication function
        i = admins.Search(admins.root,admin(name,password))
        if(i != None and i.name == name):
            if (i.password == hash(password).get_hash()):
                return True 
        else:
            return False

    def menu(self):                                                                         #admin functions menu
        print("\n\tA D M I N")
        print("\n\t\t1 - Add Route")
        print("\t\t2 - Delete Route")
        print("\t\t3 - Change Route")
        print("\t\t4 - View Routes")
        print("\t\t5 - View Admins")
        print("\t\t6 - View Users")
        print("\t\tExit")

    def login_menu(self):                                                                   #admin login menu
        print("\n\tA D M I N")
        print("\n\t\t1 -  Login")
        print("\t\t2 - Create Account")
        print("\t\tExit")
        choice=int(input("\n\t\tEnter Choice : "))
        if(choice == 1):
            self.login()
        elif(choice == 2):
            self.create_acc()

    def invalid_menu(self):                                                                 #invalid login menu
        print("\n\tI N V A L I D    L O G I N")
        print("\n\t\t1 - Try Again")
        print("\t\t2 -  Create Account")
        return int(input("\t\tEnter Choice : "))
    
    def func(self):                                                                         #menu driven functions for admin login
        self.menu()
        choice = int(input("\n\t\tEnter Choice : "))
        if (choice == 1):
            x = route.add_menu()
            route.add_route(x[0],x[1],x[2],x[3],x[4])
            self.func()
        elif (choice == 2):
            x = route.del_menu()
            route.del_route(x[0],x[1])
            self.func()
        elif (choice == 3):
            x = route.set_menu()
            route.set_route(x[0],x[1],x[2],x[3],x[4])
            self.func()
        elif (choice == 4):
            x = route.menu()
            if (x == 1):
                route.show_dist()
            elif (x == 2):
                route.show_time()
            elif (x == 3):
                route.show_cost()
            else:
                return
            self.func()
        elif (choice == 5):
            print("\n\tA D M I N S\n")
            admins.show(admins.root)
            self.func()
        elif (choice == 6):
            print("\n\tU S E R S\n")
            users.show()
            self.func()
        else:
            return

#user - stores all the user login details and the functionalities

class user:

    def __init__(self,name,password):                                                       #stores the user login details in the form of hashtable
        self.name=name
        self.password=hash(password).get_hash()

    def login(self):                                                                        #user login function
        print("\n\tL O G I N")
        name = input("\n\t\tEnter Name : ")
        password = getpass.getpass(prompt="\t\tEnter Password : ")
        if (self.authenticate(name,password)==True):
            self.func()
        else:
            x = self.invalid_menu()
            if (x==1):
                self.login()
            elif (x==2):
                self.create_acc()
    
    def authenticate(self,name,password):                                                   #user login authentication
        x = users.get(hash(password).get_hash())
        if(x != None and x.name == name):
            return True
        else:
            return False
    
    def create_acc(self):                                                                   #creating new user login
        print("\n\tC R E A T E    A C C O U N T")
        users.add(user(input("\n\t\tEnter Name : "),
        getpass.getpass(prompt="\t\tEnter Password : ")))        
        self.login()

    def menu(self):                                                                         #user functionalities menu
        print("\n\tU S E R\n")
        print("\t\t1 - Flights From")
        print("\t\t2 - Flights To")
        print("\t\t3 - Fastest Route")
        print("\t\t4 - Cheapest Route")
        print("\t\tExit")
    
    def login_menu(self):                                                                   #user login menu
        print("\n\tU S E R")
        print("\n\t\t1 - Login")
        print("\t\t2 - Create Account")
        print("\t\tExit")
        choice=int(input("\n\t\tEnter Choice : "))
        if(choice == 1):
            self.login()
        elif(choice == 2):
            self.create_acc()

    def invalid_menu(self):                                                                 #invalid user login menu
        print("\n\tI N V A L I D    L O G I N")
        print("\n\t\t1 - Try Again")
        print("\t\t2 -  Create Account")
        return int(input("\n\t\tEnter Choice : "))
    
    def func(self):                                                                         #menu driven function for user login
        self.menu()
        choice = int(input("\n\t\tEnter Choice : "))
        if (choice == 1):
            route.cities()
            x = int(input("\n\tEnter Choice : "))
            print("\n\tF L I G H T S\n\n\tFrom\t",route.name[x-1],"\n\tTo")
            route.print_from(x)
            self.func()
        elif (choice == 2):
            route.cities()
            x = int(input("\n\tEnter Choice : "))
            print("\n\tF L I G H T S\n\n\tTo\t",route.name[x-1],"\n\tFrom")
            route.print_to(x)
            self.func()
        elif (choice == 3):
            x = route.time_menu()
            l = []
            route.get_flight_t(l,x[0]-1,x[1]-1)
            route.print_route(l)
            self.func()
        elif (choice == 4):
            x = route.cost_menu()
            l = []
            route.get_flight_c(l,x[0]-1,x[1]-1)
            route.print_route(l)
            self.func()
        else:
            return

#flight - stores the flight details 

class flight:

    def __init__(self,src,dst):                                                             #storing the flight details
        self.src = src+1
        self.dst = dst+1
        self.dist = route.get_dist(src,dst)
        self.time = route.get_time(src,dst)
        self.cost = route.get_cost(src,dst)

def add_data():                                                                             #function to add few test users
    global route,admins,users,test_admin,test_user
    route = graph()
    admins = splaytree()
    users = hashtable()
    test_admin = admin("Steve","V")
    test_admin2 = admin("Prost","0")
    test_admin3 = admin("Micheal","47")
    test_admin4 = admin("Senna","27")
    test_admin5 = admin("Kimi","7")
    admins.insert(test_admin)
    admins.insert(test_admin2)
    admins.insert(test_admin3)
    admins.insert(test_admin4)
    admins.insert(test_admin5)
    test_user = user("Max","33")
    test_user2 = user("Gasly","10")
    test_user3 = user("Ricciardo","3")
    test_user4 = user("Vettel","5")
    test_user5 = user("Lewis","44")
    users.add(test_user)
    users.add(test_user2)
    users.add(test_user3)
    users.add(test_user4)
    users.add(test_user5)

def start():                                                                                #invokes the actual program
    print("\n\tA I R L I N E     E N Q U I R Y     S Y S T E M")
    print("\n\t\tE N Q - A I R")
    print("\n\t\t1 - Admin")
    print("\t\t2 - User")
    print("\t\tExit")
    x = int(input("\n\tEnter Choice : "))
    if (x==1):
        test_admin.login_menu()
        start()
    elif (x==2):
        test_user.login_menu()
        start()
    else:
        return