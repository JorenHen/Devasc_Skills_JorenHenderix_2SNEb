ACLnummer = int(input("Wat is het IPv4 ACL nummer? "));
if ACLnummer >= 1 and ACLnummer <= 99:
    print("Dit is een standard IPv4 ACL.");
elif ACLnummer >=100 and ACLnummer <= 199:
    print("Dit is een extended IPv4 ACL.");
else:
    print("Dis is geen standard of extended IPv4 ACL.");