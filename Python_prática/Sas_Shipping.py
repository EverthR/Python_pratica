def ground_shipping(weight):
	if(weight <= 2):
		cost = (weight*1.5) 
		
	elif(2 < weight <= 6):
		cost = (weight*3) 
		
	elif(6 < weight <= 10):
		cost = (weight*4) 

	else:
		cost = (weight*4.75) 

	return cost + 20

premium_shipping = 125.00

def drone_shipping(weight):
	if(weight <= 2):
		cost = (weight*4.5) 
		
	elif(2 < weight <= 6):
		cost = (weight*9) 
		
	elif(6 < weight <= 10):
		cost = (weight*12) 

	else:
		cost = (weight*14.25) 

	return cost 

def cheapest_shipping(weight):
        ground = ground_shipping(weight)
        premium = premium_shipping
        drone = drone_shipping(weight)

        #print(ground)
        #print(premium)
        #print(drone)

        if (ground < premium) and (ground < drone):
                method = "The best shipping option for you is the GROUND SHIPPING"
                price = ground

                print(method)
                print("The cost is", price)

                #return True
                
        elif (premium < ground) and (premium < drone):
                method = "The best shipping option for you is the PREMIUM SHIPPING"
                price = premium

                print(method)
                print("The cost is", price)
                
                #return True
        else:
                method = "The best shipping option for you is the DRONE SHIPPING"
                price = drone

                print(method)
                print("The cost is", price)
                
                #return True
                
        
       

        
                
