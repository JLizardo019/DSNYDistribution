"""
Data Visualization
By: Julie Lizardo
"""
import math


def recyclingAnalysis(name):

    num_bins = 0
    locations =[]
    # 0 indoor, 1 outdoor, 2 subproperty, 3 Greenthumb
    sitetypes = [0]*4

    # number of
    for bin in public_bins:
        #print(bin[0])
        if bin[0] == name:
            site = bin[1].strip()
            if site == "Indoor":
                sitetypes[0]+=1
            elif site == "Outdoor":
                sitetypes[1]+=1
            elif site  == "Subproperty":
                sitetypes[2] +=1
            elif site == "Greenthumb":
                sitetypes[3] +=1
            # else:
            #     print("Something went wrong while analyzing site types")

            try:
                locations.append([float(bin[4].strip()), float(bin[5].strip())])
                num_bins += 1
            except:
                print("No coordinates", bin)
    avg_dis, min_dis, max_dis = radial_distance(locations)

    # print(sitetypes, sum(sitetypes), num_bins, len(public_bins))
    return [avg_dis, min_dis, max_dis, sitetypes, num_bins]


def trashAnalysis(name2):

    num_bins = 0
    locations =[]
    # 0 DSNY-Owned, 1 BID-Owned, 2 Private-Owned
    sitetypes = [0]*3

    # number of
    for bin in public_bins2:
        borough =""
        # 7 operation zones (Manhattan, Bronx, Brooklyn North, Brooklyn South, Queens West, Queens East, and Staten Island)
        if bin[0][0:2] == "MN":
            borough = "Manhattan"
        elif bin[0][0:2] == "BX":
            borough = "Bronx"
        elif bin[0][0:2].strip() == "BK":
            borough = "Brooklyn"

        elif bin[0][0:2] == "QW" or bin[0][0:2] == "QE":
            borough = "Queens"
        elif bin[0][0:2] == "SI":
            borough = "Staten Island"
        # else:
            # print("Something went wrong while analyzing borough names")
            # print(bin[0])

        if borough == name2:
            site = bin[6].strip()
            if site == "DSNY-owned":
                sitetypes[0]+=1
            elif site == "BID-owned":
                sitetypes[1]+=1
            elif site  == "Privately owned":
                sitetypes[2] +=1
            # else:
            #     print("Something went wrong while analyzing site types")

            if (bin[10] != ""):
                locations.append([float(bin[10].strip()), float(bin[11].strip())])
                num_bins += 1
            # else:
            #     print("No coordinates", bin)

    avg_dis, min_dis, max_dis = linear_distance(locations)

    # print(sitetypes, sum(sitetypes), num_bins, len(public_bins))
    return [avg_dis, min_dis, max_dis, sitetypes, num_bins]


def refuseAnalysis():
    refuse = [0] * 5
    numlines=0

    # number of
    for line in refuse_data:
        if len(line)>1:
            numlines+=1
            site = line[1].strip()
            if site == "Manhattan":
                refuse[0] += float(line[3])
            elif site == "Queens":
                refuse[1] += float(line[3])
            elif site == "Brooklyn":
                refuse[2] += float(line[3])
            elif site == "Staten Island":
                refuse[3] += float(line[3])
            elif site == "Bronx":
                refuse[4] += float(line[3])

    for num in range(len(refuse)):
        refuse[num] /=numlines


    return refuse


def radial_distance(location_list):
    dist =[]

    for pos in range(0,len(location_list)):
        for pos2 in range(pos+1,len(location_list)):

            # the ‘haversine’ formula to calculate the great-circle distance between two points
            #https: // www.movable - type.co.uk / scripts / latlong.html
            radius = 6371* (10**3) # meters of earth radius
            lat1 = math.radians(location_list[pos][0])
            long1 = math.radians(location_list[pos][1])

            lat2 = math.radians(location_list[pos2][0])
            long2 = math.radians(location_list[pos2][1])
            del_lat = math.radians(lat2-lat1)
            del_long = math.radians(long2 - long1)

            a = math.sin(del_lat / 2) * math.sin(del_lat / 2) + math.cos(lat1) * math.cos(lat2) * math.sin(del_long / 2) * math.sin(del_long / 2)

            c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
            d = radius * c
            dist.append(d)

    return sum(dist)/len(dist), min(dist),max(dist)


def linear_distance(location_list):
    dist =[]

    for pos in range(0,len(location_list)):
        for pos2 in range(pos+1,len(location_list)):

            x1 = math.radians(location_list[pos][0])
            y1 = math.radians(location_list[pos][1])

            x2 = math.radians(location_list[pos2][0])
            y2 = math.radians(location_list[pos2][1])

            d = math.sqrt((x2-x1)**2 +(y2-y1)**2)
            dist.append(d)


    return sum(dist)/len(dist), min(dist),max(dist)

########### Public Recycling Bins ###########
# Data in latitude and longitude (updated September 10, 2018)
file1 = open("Public_Recycling_Bins.tsv", "r")
data = file1.read()
file1.close()
rawData = data.split("\n")

# Columns: 0 Borough, 1 Site type, 2 Park/Site Name, 3  Address, 4 Latitude, 5 Longitude
public_bins = []

# clean data by bin
for pos in range(1,len(rawData)):
    line = rawData[pos].split("\t")

    public_bins.append(line)



########### Public Trash Cans ###########
# Data in New York State Plane Coordinate System (updated Oct 7, 2019)

file2 = open("Public_Trash_Bins.csv", "r")
data2 = file2.read()
file2.close()
rawData2 = data2.split("\n")


# Columns: 0 Borough, 6 Site type,... 10 Latitude, 11 Longitude
public_bins2 = []

# clean data by bin
for pos in range(1,len(rawData2)):
    line = rawData2[pos].split(",")

    public_bins2.append(line)



########### Monthly Refuse Tonnage ###########
# (updated November 8, 2019)

file3 = open("DSNY_Monthly_Tonnage_Data.tsv", "r")
data3 = file3.read()
file3.close()
rawData3 = data3.split("\n")

# Columns: 1 Borough, 3 refuse (tons)
refuse_data = []

# clean data by bin
for pos in range(1,len(rawData3)):
    line = rawData3[pos].split("\t")

    refuse_data.append(line)



########### Saving Results ###########

result_file = open("Results.txt", "w")

bronx_info= recyclingAnalysis("Bronx")
man_info= recyclingAnalysis("Manhattan")
queen_info= recyclingAnalysis("Queens")
brook_info= recyclingAnalysis("Brooklyn")
stat_info= recyclingAnalysis("Staten Island")

bronx_info2= trashAnalysis("Bronx")
man_info2= trashAnalysis("Manhattan")
queen_info2= trashAnalysis("Queens")
brook_info2= trashAnalysis("Brooklyn")
stat_info2= trashAnalysis("Staten Island")

refuse_facts = refuseAnalysis()

# [0 # of recycling bins, 1 #avg distance , 2 site types], [0 # of trash bins, 1 #avg distance , 2 site types], [tons of waste]

result_file.write("Brooklyn\t"+ str(brook_info)+"\t" + str(brook_info2)+ "\t"+ str(refuse_facts[2])+ "\n")
result_file.write("Bronx\t"+ str(bronx_info) + "\t"+ str(bronx_info2)+ "\t"+ str(refuse_facts[4])+"\n")
result_file.write("Manhattan\t"+ str(man_info)+"\t"+ str(man_info2)+ "\t"+ str(refuse_facts[0])+"\n")
result_file.write("Queens\t"+ str(queen_info)+ "\t" +str(queen_info2)+"\t"+str(refuse_facts[1])+"\n")
result_file.write("Staten Island\t"+ str(stat_info)+"\t"+ str(stat_info2)+"\t"+str(refuse_facts[3]))


result_file.close()

print("All done!")





