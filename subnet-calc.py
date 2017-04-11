def main():
    ip = int(raw_input("IP :"))
    # cidr = int(raw_input("cidr "))
    mask = int(raw_input("Network Mask :"))
    addclass = 24
    cidr = int(cider(mask)) + addclass
    print "CIDR :", cidr

    nets = (2**(cidr - addclass))
    hosts = (2**(32 - cidr)) - 2
    neta = ip - (ip % (256 - mask))
    nneta = neta + (256 - mask)

    print "Network -------- : ", neta
    print "First -----------: ", neta + 1
    print "Last ------------: ", nneta - 2
    print "Broadcast -------: ", nneta - 1
    print "Next Network ----: ", nneta
    print "# of Hosts ------: ", hosts
    print "# of Networks ---: ", nets

def cider(mask):
    cidr = 0
    modi = 128
    while mask > 0:
        # print "cidr :", cidr
        # print "Mask :", mask
        # print "mod :", modi

        mask = (mask % modi)
        modi = (modi / 2)
        cidr = cidr + 1
    return cidr

main()