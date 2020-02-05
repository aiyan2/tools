#2020-0205- debug and run @166( devqa.lab), to simualte the 65535 length of grps for user allGrp
# the max length of win-dc groups is 64, so has to create ~1000 groups 
Import-Module ActiveDirectory
$groups = Import-Csv 'c:\ft\grp.csv'
#$SEED = 'AAAA50123456789012345678901234567890123456789512345678961234'
#$SEED = 'ABAA50123456789012345678901234567890123456789512345678961234'
$SEED = 'ANAA50123456789012345678901234567890123456789512345678961234'
foreach ($group in $groups) {
#New-ADGroup -Name agp$group.name -Path ?CN=Domain Users,CN=Users,DC=devqa,DC=lab? -Description ?Bulk? -GroupCategory Security -GroupScope Universal -Managedby BC
$gName  = $SEED + $group.name 
Get-ADGroup "Domain Users" -Properties Description | New-ADGroup -Name $gName  -SamAccountName $gName  -GroupCategory Distribution -PassThru

}



### grp.csv content

name
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
..
50 
...
###
