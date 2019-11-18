Import-Module ActiveDirectory
$groups = Import-Csv ‘c:\ft\grp.csv‘
foreach ($group in $groups) {
#New-ADGroup -Name agp$group.name -Path “CN=Domain Users,CN=Users,DC=devqa,DC=lab” -Description “Bulk” -GroupCategory Security -GroupScope Universal -Managedby BC

Get-ADGroup "Domain Users" -Properties Description | New-ADGroup -Name $group.name -SamAccountName $group.name  -GroupCategory Distribution -PassThru

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
...
###